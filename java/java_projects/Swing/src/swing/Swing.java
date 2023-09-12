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
public class Swing extends JFrame implements ActionListener{
    
    private int counts = 0;
    private static JLabel label;
    private static JFrame frame;
    private static JButton button;
    private static JPanel panel;
    
    
    
    public static void GUI(){
        frame = new JFrame();
        
        
        panel = new JPanel();
        
        button = new JButton("Click me");
        Swing Listener = new Swing();
        button.addActionListener(Listener);
        
        label = new JLabel("Number on Clicks: 0");
        
        
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
