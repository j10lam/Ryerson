/**
* Assignment #2 - Machine Learning-Computer Vision
* 
* @author Jonathan Lam
* @version 1.0
*/

/**
Import
*/
import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.*;
import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.util.Arrays;

/**
The class bonus implements the feedforward method: calculating perceptron ouput layer by
layer using the previous layer as the new input to approximate the integer values in a set of images
and produces the classification rate of this method
*/
public class bonus
{
    /**
    main(args) approximates image integer value.
    @param args Unused.
    @return void Nothing.
    */
    public static void main(String[] args) throws FileNotFoundException, java.io.IOException
    {
        // Variable Initialization - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        final int HIDDEN_ROWS = 300;
        final int HIDDEN_VALUES = 785;
        final int OUTPUT_ROWS = 10;
        final int OUTPUT_VALUES = 301;

        File hidden = new File("hidden-weights.txt");
        File output = new File("output-weights.txt");
        File images = new File("labels.txt");

        Scanner scan_hidden = new Scanner(hidden);
        Scanner scan_output = new Scanner(output);
        Scanner scan_images = new Scanner(images);

        int num_lines = 0;
        double num_correct = 0;
        double rate;
        
        double[][] hidden_weights = construct(scan_hidden, HIDDEN_ROWS, HIDDEN_VALUES);
        double[][] output_weights = construct(scan_output, OUTPUT_ROWS, OUTPUT_VALUES);

        // Body of Method - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        while (scan_images.hasNextLine())
        {
            File dest = new File("numbers/" + scan_images.next());
            int expected = scan_images.nextInt();

            double[] pixels = makePixels(dest);
            double[] hidden_perceptron = perceptron(pixels, hidden_weights);
            double[] output_perceptron = perceptron(hidden_perceptron, output_weights);

            int prediction = maxValue(output_perceptron);
            if (prediction == expected) {num_correct++;};
            
            scan_images.nextLine();

            num_lines++;
        }

        rate = ((num_correct / num_lines) * 100.0);
        System.out.printf("The classification rate is %.2f%%.\n", rate);
    }

    /**
    makePixels(dest) creates a pixel value array from an image and rescales
                     each element.
    @param dest Contains destination of image of type File.
    @return doublep[] An array of type double containing pixel values rescaled.
    @see java.io.IOException
    */
    public static double[] makePixels(File dest) throws java.io.IOException
    {
        // Variable Initialization -- - - - - - - - - - - - - - - - - - - - 
        BufferedImage img = ImageIO.read(dest);
        double[] dummy = null;
        final double FACTOR = 255.0;


        // Body of Method - - - - - - - - - - - - - - - - - - - - - - - - - 
        double[] pixels = img.getData().getPixels(0, 0, img.getWidth(), img.getHeight(), dummy);

        for (int i = 0; i < pixels.length; i++) // to rescale elements in pixels
        {
            pixels[i] /= FACTOR;
        }
        
        return pixels;
    }
    
    /**
    construct(scanner, row, col) takes in values of type double from scanner and
                                 produces a multi-dimensional array of type double
                                 with set size row by col.
    @param scanner Of type Scanner, returns next value in associated value.
    @param row Set row size of array to be returned.
    @param col Set column size of array to be returned.
    @return double[][] A multi-dimensional array containing weights (and bias) of each neuron
             in corresponding layers.
    */
    public static double[][] construct(Scanner scanner, int row, int col)
    {
        // Variable Initialization - - - - - - - - - - - - - - - - - - -
        double[][] layer = new double[row][col];
        
        // Body of Method - - - - - - - - - - - - - - - - - - - - - - - -
        for (int r = 0; r < row; r++)
        {
            for (int c = 0; c < col; c++)
            {
                layer[r][c] = scanner.nextDouble();
            }
            scanner.nextLine();
        }

        return layer;
    }

    /**
    perceptron(input, weights) calculates the perceptron for each neuron
                               corresponding to their respective layers.
    @param input An array of perceptron corresponding to previous layer.
    @param weights A multi-dimensional array of weights for each neuron 
                          in their resspective layers.
    @return double[] An array of calculated perceptrons.
    */
    public static double[] perceptron(double[] input, double[][] weights) 
    {
        // Variable Initialization - - - - - - - - - - - - - - - - - - - 
        int cols = input.length;
        int rows = weights.length;
        double[] output = new double[rows];

        // Body of Method - - - - - - - - - - - - - - - - - - - - - - - -
        for (int r = 0; r < rows; r++)
        {
            double sum = 0;

            for (int c = 0; c < cols; c++) 
            {
                sum += input[c]*weights[r][c];
            }

            sum += weights[r][cols];
            output[r] = 1.0 / (1.0 + Math.exp(sum * -1.0));
        }
        
        return output;
    }

    /**
    maxValue(outputs) find the greatest element in outputs
    @param outputs Contains an array of output neurons of type double
    @returns int The index corresponding to the greatest element in outputs
    */
    public static int maxValue(double[] outputs)
    {
        // Variable Initialization - - - - - - -
        int index = 0;
        double max = outputs[0];

        // Body of Method - - - - - - - - - - - -
        for (int i = 0; i < outputs.length; i++)
        {
            if (outputs[i] > max)
            {
                max = outputs[i];
                index = i;
            }
        }

        return index;
    }

}

