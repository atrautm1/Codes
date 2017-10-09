package lab2;

import java.util.ArrayList;
import java.util.Random;

public class Random_DNA_Generator {

	public static void main(String[] args) {
		
		// dnaList for storing the DNA sequence generated if used for later analysis 
		ArrayList<Integer> dnaList = new ArrayList<Integer>();
		
		// String variable to append and print DNA bases
		String dnaSeq = "";
		
		// Stores the count of AAA
		int tripleAAACount = 0;
		
		// Instance of random class
		Random random = new Random();
		
		// for x in specified DNA length at 3000 bp, add an integer in between 1-4
		for (int x=0;x<3000;x++) {
			dnaList.add(random.nextInt(4) + 1);
		}
		
		// for every item in dnaList, check number, set to dna base
		for (int x = 0; x < dnaList.size() ; x++) {
			if (dnaList.get(x) == 1) {
				dnaSeq += "A";
			}
			else if (dnaList.get(x) == 2) {
				dnaSeq += "G";
			}
			else if (dnaList.get(x) == 3) {
				dnaSeq += "T";
			}
			else if (dnaList.get(x) == 4) {
				dnaSeq += "C";
			}
			// If kmer length = 3, check if dnaSeq is "AAA", print out dnaSeq, and reset the variable
			if (dnaSeq.length() == 3) {
				if (dnaSeq.equals("AAA")) {
					tripleAAACount++;
				}
				System.out.println(dnaSeq);
				dnaSeq = "";
			}
			
		}
		System.out.println(tripleAAACount);
	}

}
