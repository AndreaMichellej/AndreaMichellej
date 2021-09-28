// Andrea Joseph
// C00166106
// CMPS 260
// Programming Assignment: 2
// Due Date: September 21, 2020
// Program Description: Get user name, age, driver's test score
// determine whether they are able to obtain a license and if
// they are eligible to vote, then display a summary message
// Certificate of Authenticity:
// I certify that the code in the method function main of this
// project is entirely my own work.


package com.company;

import java.util.Scanner;
public class Main {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        //Get User Input
        System.out.print("Enter a name: ");
        String name = in.nextLine();

        System.out.print("Enter an age: ");
        int age = in.nextInt();

        System.out.print("Enter a driver's test score: ");
        int testScore = in.nextInt();

        //While Loop
        System.out.print("Would you like to continue (Yes or No)? ");
        String answer = in.next();

        while (answer.equals("Yes")){
            if (age <= 15) {
                System.out.println(name + " can not drive and is not eligible to vote.");
            } else if (age == 16) {
                System.out.println(name + " can drive with a learner's permit and is not eligible to vote.");
            } else if (age == 17 && testScore >= 32) {
                System.out.println(name + " can drive with a full license and is not eligible to vote.");
            } else if (age == 17 && testScore < 32) {
                System.out.println(name + " can not drive with a full license ans is not eligible to vote.");
            } else if (age >= 18) {
                if (testScore < 32)
                    System.out.println(name + " can not drive with a full license and is eligible to vote.");
                else if (testScore > 40) {
                    System.out.println("Invalid Input!");
                } else System.out.println(name + " can drive with a full license and is eligible to vote.");
            }
            System.out.print("Would you like to continue (Yes or No)? ");
            answer = in.next();
            if (answer.equals("No") || (!answer.equals("Yes"))) {
                break;
            } else {
                Scanner input = new Scanner(System.in);
                System.out.print("Enter a name: ");
                name = input.nextLine();
                System.out.print("Enter an age: ");
                age = input.nextInt();
                System.out.print("Enter a driver's test score: ");
                testScore = input.nextInt();


            }
        }



    }
}
