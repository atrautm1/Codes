package lab3;

import java.util.Random;

import com.sun.xml.internal.ws.util.StringUtils;

public class Amino_Acid_Quiz {
	
	private static boolean isNum(String s) {
		if (s.matches("\\d+")) {
			return true;
		}
		else {
			return false;
		}
	}

	public static void main(String[] args) throws Exception{
		
		Random random = new Random();
		
		String[] aaCodes = 
		{ "A","R", "N", "D", "C", "Q", "E", 
		"G",  "H", "I", "L", "K", "M", "F", 
		"P", "S", "T", "W", "Y", "V" };

		String[] aaNames = {
		"Alanine","Arginine", "Asparagine", 
		"Aspartic acid", "Cysteine",
		"Glutamine",  "Glutamic acid",
		"Glycine" ,"Histidine","Isoleucine",
		"Leucine",  "Lysine", "Methionine", 
		"Phenylalanine", "Proline", 
		"Serine","Threonine","Tryptophan", 
		"Tyrosine", "Valine"};
		
		//Allow user to enter in a specific time in seconds
		System.out.println("How long (in seconds) would you like this quiz to last? Press enter for default : ");
		String dur = System.console().readLine();
		
		//Initialize duration integer
		int duration;
		
		//Check if user input is numeric
		if (isNum(dur)) {
			duration = Integer.parseInt(dur) * 1000;
		}
		else {
			duration = 30;
		}
		
		//Initialize score
		int score = 0;
		
		//Initial Start Time
		long startTime = System.currentTimeMillis();
	 
		//As long as 30 seconds hasn't elapsed
		while (System.currentTimeMillis() - startTime < duration) {
			
			//Variable for calling the amino acid
			int x = random.nextInt(20);
			
			System.out.println("What is the one-letter code for: " + aaNames[x]);
			
			//User input
			String userAA = System.console().readLine().toUpperCase();
			
			//Check if user input is correct
			if (userAA.equals(aaCodes[x])) {
				score += 1;
			}
			//Allow user to exit
			else if (userAA.equals("QUIT")) {
				System.out.println("Your score was: "+ score);
				System.exit(0);
			}
			//If user input is wrong
			else {
				System.out.println("Sorry, the codon was actually: " + aaCodes[x]);
				System.out.println("Your score was: "+ score);
				System.exit(0);
			}
		}
		System.out.println("Time expired! Your score was: " + score);
	}

}
