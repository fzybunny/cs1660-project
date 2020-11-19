import java.awt.*;
import javax.swing.*;

public class ProjectGUI extends JFrame {
	private final String GUI_TITLE = "Data Science Toolbox Project";
	private final String[] APP_NAMES = {
		"RStudio",
		"Spyder",
		"IBM SAS",
		"Git",
		"Jupyter Notebook",
		"Orange",
		"Visual Studio Code",
		"Apache Hadoop",
		"Apache Spark",
		"Tableau",
		"SonarQube and SonarScanner",
		"Tensorflow",
		"Markdown"
	};

	private final JButton[] app_buttons = new JButton[APP_NAMES.length];

	public ProjectGUI() {
		super();
		this.setTitle(GUI_TITLE);
		this.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
		this.setLayout(new FlowLayout());

		for (int i = 0; i < APP_NAMES.length; i++) {
			app_buttons[i] = new JButton(APP_NAMES[i]);
			this.add(app_buttons[i]);
		}

		this.pack();
		this.setVisible(true);
	}

	public static void main(String[] args) throws Exception {
		new ProjectGUI();
	}
}


/*
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Sample extends JFrame {
	private final JButton b = new JButton();

	public Sample() {
		super();
		this.setTitle("HelloApp");
		this.getContentPane().setLayout(null);
		this.setBounds(100, 100, 180, 140);
		this.add(makeButton());
		this.setVisible(true);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
	}

	private JButton makeButton() {
		b.setText("Click me!");
		b.setBounds(40, 40, 100, 30);
		b.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				JOptionPane.showMessageDialog(b, "Hello World!");
			}
		});
		return b;
	}

	public static void main(String[] args) {
		// Swing calls must be run by the event dispatching thread.
		SwingUtilities.invokeAndWait(() -> new Sample());
	}
}
*/
