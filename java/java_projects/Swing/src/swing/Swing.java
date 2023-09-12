/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package swing;
import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

/**
 *
 * @author Nico
 */
public class Swing implements ActionListener{
    
    private int counts = 0;
    private JLabel label;
    private JFrame frame;
    
    
    public static void GUI(){
        JFrame frame = new JFrame();
        
        
        JPanel panel = new JPanel();
        
        
        JButton button = new JButton("Click me");
        
        button.addActionListener(this);
        
        JLabel label = new JLabel("Number on Clicks: 0");
        
        
        panel.setBorder(BorderFactory.createEmptyBorder(30, 30, 10, 30));
        panel.setLayout(new GridLayout(0, 1));
        panel.add(button);
        panel.add(label);
        
        frame.add(panel, BorderLayout.CENTER);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("GUI");
        frame.pack();
        frame.setVisible(true);
        
    }
    
    public static void main(String[] args) {
        // TODO code application logic here
        GUI();
        
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        counts++;
        label.setText("Number of clicks: " + counts);
    }
    
}
