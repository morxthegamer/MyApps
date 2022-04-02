package main;

import java.awt.Dimension;

import javax.swing.*;

import java.awt.Color;

public class GUIApp implements Runnable {

    private String title;
    private int width, height;
    private JFrame frame;
    private JButton button;
    private JPanel panel;
    private JTextField tf;
    private Thread thread;
    private boolean running = false;

    public GUIApp(String title, int width, int height) {
        this.title = title;
        this.width = width;
        this.height = height;

        init();
    }

    private void init() {
        frame = new JFrame(title);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setFocusable(true);
        frame.setVisible(true);
        frame.setResizable(false);
        frame.setSize(width, height);
        frame.setLocationRelativeTo(null);
        frame.setBackground(Color.black);
    }

    public void createButton() {
        button = new JButton("Click this.");
        button.setSize(50, 50);
    }

    public void createPanel() {

    }

    public void createTF() {

    }

    public synchronized void start() {
        if (running) return;

        running = true;

        thread = new Thread(this);
        thread.start();
    }

    public void run() {
        createButton();
        createPanel();
        createTF();
    }

    public synchronized void stop() {
        if (!running) return;

        try {
            thread.join();
            running = false;
        } catch (Exception err) {
            err.printStackTrace();
        }
    }
}
