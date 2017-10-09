package lab4;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

public class FastaSequence {
	private final String header;
	private final String sequence;
	
	public FastaSequence(String header, String sequence) {
		this.header = header;
		this.sequence = sequence;
	}
	
public static void main(String[] args) throws Exception {
		/*
		//Fasta file to read
	
		File lab4In = new File("/Users/atrautm1/Desktop/gradFall2017/programming/rando.fasta");
		System.out.println(lab4In.getAbsolutePath());
		
		List<FastaSequence> fastaList = 
				FastaSequence.readFastaFile(lab4In.getAbsolutePath());
		
		// For each sequence in the file, print the header, sequence and the GC percent
		for (FastaSequence seq : fastaList) {
			System.out.println(seq.getHeader());
			System.out.println(seq.getSequence());
			System.out.println("The GC percent is: "+ seq.getGCRatio()+"%");
		} 
		
		File lab5Input = new File("/Users/atrautm1/Desktop/gradFall2017/programming/seqsIn.txt");
		File lab5Output = new File("/Users/atrautm1/Desktop/output.txt");
		writeUnique(lab5Input, lab5Output);
		*/
		
		File lab6Input = new File("/Users/atrautm1/Desktop/gradFall2017/programming/seqsIn.txt");
		File lab6Output = new File("/Users/atrautm1/Desktop/output.tsv");
		
		spreadsheetWriter(lab6Input, lab6Output);
		
	}

	public static List<FastaSequence> readFastaFile(String filepath) throws Exception {
		// Read in file as bufferedReader object called fasta
		BufferedReader fasta = new BufferedReader(new FileReader(new File(filepath)));
		
		// Build new list object of fasta sequences in file
		List<FastaSequence> myList = new ArrayList<FastaSequence>();
		
		// Initialize variables for header and sequence
		String header = "";
		StringBuffer sequence = new StringBuffer();
		
		//For each line in the file
		for(String line = fasta.readLine(); line != null; line=fasta.readLine()) {
			
			// If the header is blank, beginning of file, should only happen once per file
			if (header.equals("")) {
				// Check if the file starts with a header, if not, throw exception
				if (!line.startsWith(">")) {
					throw new Exception("Your first sequence appears to be missing a header!");
				}
				header = line.substring(1);
			}
			// Whenever a new header appears, make a new fastaSequence with current header and sequence in memory and add it to the list "myList" 
			else if (line.startsWith(">")) {
				FastaSequence fs = new FastaSequence(header,sequence.toString());
				myList.add(fs);
				// Set header to current line, and reset sequence
				header = line.substring(1);
				sequence.setLength(0);
			}
			// All other lines should be part of the sequence, so append it in uppercase to the current sequence
			else {
				sequence.append(line.toUpperCase());
			}
		}
		// Header and sequence still in memory aren't added to list, so add them, close the file, and return "myList"
		FastaSequence fs = new FastaSequence(header,sequence.toString());
		myList.add(fs);
		fasta.close();
		return myList;
	}
		
		public String getHeader() {
			return this.header;
		}
		
		public String getSequence() {
			return this.sequence;
		}
		
		public Float getGCRatio() {
			// Initialize the count; ah, ah, ah
			int countGC = 0;
			float seqLen = sequence.length();
			// For every char in the sequence, check if the character is equal to G or C and add one to the count if so
			for (int x = 0; x < this.sequence.length(); x++){
				 char base = this.sequence.charAt(x);
				 if (base == 'C' || base =='G'){
					 countGC++;
				 }
			 }
			// Return the ratio as a percentage
			 return ((float)countGC/seqLen) * 100f;
		}
	
		public static void writeUnique(File inFile, File outFile ) throws Exception {
			
			BufferedWriter fileOut = new BufferedWriter(new FileWriter(outFile));
			
			List<FastaSequence> sequenceList = FastaSequence.readFastaFile(inFile.getAbsolutePath());
			
			HashMap<String, Integer> myHashMap = new HashMap<String, Integer>();
			
			for (FastaSequence seq : sequenceList) {
				String sequence = seq.getSequence();
				if (!myHashMap.containsKey(sequence)) {
					myHashMap.put(sequence, 1);
				}
				else {
					myHashMap.put(sequence, myHashMap.get(sequence) + 1);
				}
			}
			
			List<Entry<String, Integer>> myList = new ArrayList<Entry<String, Integer>>(myHashMap.entrySet());
			
			myList.sort((o1,o2)->((Comparable<Integer>) ((Map.Entry<String,Integer>)(o1)).getValue()).compareTo((Integer) ((Map.Entry<String, Integer>)(o2)).getValue()));
			
			for (Entry<String, Integer> entry : myList) {
				fileOut.write(">" + entry.getValue());
				fileOut.newLine();
				fileOut.write(entry.getKey());
				fileOut.newLine();
				
			}
			
			// for (String key : myHashMap.keySet()) {
			//	System.out.println(key + " = " + myHashMap.get(key));
			//}
			
			fileOut.close();
		    }

		public static void spreadsheetWriter(File inFile, File outFile) throws Exception {
			BufferedWriter fileOut = new BufferedWriter(new FileWriter(outFile));
			List<FastaSequence> sequenceList = FastaSequence.readFastaFile(inFile.getAbsolutePath());
			
			//Final HashMap structure for the data 
			LinkedHashMap<String, Map<String,Integer>> finalHashMap = new LinkedHashMap<String, Map<String,Integer>>();
			
			double startTime = System.currentTimeMillis();
			
			//List of samples
			List<String> tokens = new ArrayList<String>();
			
			//Add samples to list (only unique ones)
			for (FastaSequence fs: sequenceList) {
				String token = fs.getHeader().split("\\s")[1];
				if (!tokens.contains(token))
					tokens.add(token);
			}
			
			//Sort list and add "Sample" for header to list
			Collections.sort(tokens);
			tokens.add(0, "Sample");
			
			//Initialize HashMap with values=0 for each sample
			for (FastaSequence fs: sequenceList) {
				String seq = fs.getSequence();
				Map<String, Integer> initMap = new HashMap<String, Integer>();
				
				for (String token : tokens) {
					initMap.put(token, 0);
				}
				finalHashMap.put(seq, initMap);
			}
			
			//Add counts
			for (FastaSequence fs: sequenceList) {
				String seq = fs.getSequence();
				String header = fs.getHeader().split("\\s")[1];
				
				Map<String, Integer> seqThing = finalHashMap.get(seq);
				
				for (String key : seqThing.keySet()) {
					if (key.equals(header)) {
						seqThing.put(header, seqThing.get(key) + 1);
					}
				}
				
				finalHashMap.put(seq, seqThing);
				
			}
			
			//Writing "for" loop uses string buffer to make the line, writes the header, and then writes each sample and count
			for (String token: tokens) {
				StringBuffer line = new StringBuffer();
				line.append(token + "\t");
				
				for (String key: finalHashMap.keySet()) {
					if (token.equals("Sample")) {
						line.append(key + "\t");
					} 
					else {
						Map<String, Integer> tokenMap = finalHashMap.get(key);
						int count = tokenMap.get(token);
						line.append(count + "\t");
						
						}
					}
				fileOut.write(line + "\n");
			}
			
			//Took around 1.2 seconds
			System.out.println("Runtime is: " + (System.currentTimeMillis() - startTime) + "ms");
			fileOut.flush();
			fileOut.close();
		
		}
}
