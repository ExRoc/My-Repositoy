package lottery;

import java.awt.Cursor;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;

import javax.swing.ImageIcon;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.Timer;

@SuppressWarnings("serial")
public class Main extends JFrame {
	ArrayList<String> name;
	JFrame itself;
	int stat;
	
	public Main() {
		super("Random");
		itself = this;
		stat = 0;
		name = new ArrayList<String>();
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setResizable(false);
		
		// set background and window size
		ImageIcon BackGroundimg = new ImageIcon("image//BackGround.png");
		JLabel BackGroundlb = new JLabel(BackGroundimg);
		getLayeredPane().add(BackGroundlb, new Integer(Integer.MIN_VALUE));
		BackGroundlb.setBounds(0, 0, BackGroundimg.getIconWidth(), BackGroundimg.getIconHeight());
		setSize(BackGroundimg.getIconWidth(), BackGroundimg.getIconHeight() + 35);
		setLocationRelativeTo(null);
		
		JPanel jp = new JPanel(null);
		jp.setOpaque(false);
		setContentPane(jp);
		
		// set labels
		JLabel namelb = new JLabel("Who?", SwingConstants.CENTER);
		jp.add(namelb);
		namelb.setBounds(190, 130, 400, 100);
		namelb.setFont(new Font("华康娃娃体W5(P)", Font.PLAIN, 100));
		
		// set timer
		Timer t = new Timer(10, new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Random rand = new Random();
				int pos = rand.nextInt() % (name.size());
				pos += name.size();
				pos %= name.size();
				namelb.setText(name.get(pos));
			}
		});
		
		ImageIcon Beginimg = new ImageIcon("image//Begin.png");
		JLabel Beginlb = new JLabel(Beginimg);
		ImageIcon Stopimg = new ImageIcon("image//Stoptmp.png");
		JLabel Stoplb = new JLabel(Stopimg);
		ImageIcon Importimg = new ImageIcon("image//Import.png");
		JLabel Importlb = new JLabel(Importimg);
		
		jp.add(Beginlb);
		Beginlb.setBounds(100,  330, Beginimg.getIconWidth(), Beginimg.getIconHeight());
		Beginlb.addMouseListener(new MouseAdapter() {
			@SuppressWarnings("deprecation")
			public void mouseEntered(MouseEvent e) {
				if(stat != 1) {
					Beginlb.setIcon(new ImageIcon("image//Begintmp.png"));
					setCursor(Cursor.HAND_CURSOR);
				}
			}
			@SuppressWarnings("deprecation")
			public void mouseExited(MouseEvent e) {
				if(stat != 1) {
					Beginlb.setIcon(Beginimg);
					setCursor(Cursor.DEFAULT_CURSOR);
				}
			}
			@SuppressWarnings("deprecation")
			public void mouseClicked(MouseEvent e) {
				if(stat != 1) {
					if(name.size() == 0) {
						NewDialog();
					} else {
						if(stat == 0) {
							t.start();
						} else {
							t.restart();
						}
						stat = 1;
						setCursor(Cursor.DEFAULT_CURSOR);
						Beginlb.setIcon(new ImageIcon("image//Begintmp.png"));
						Stoplb.setIcon(new ImageIcon("image//Stop.png"));
						Importlb.setIcon(new ImageIcon("image//importtmp.png"));
					}
				}
			}
		});
		
		jp.add(Stoplb);
		Stoplb.setBounds(295, 330, Stopimg.getIconWidth(), Stopimg.getIconHeight());
		Stoplb.addMouseListener(new MouseAdapter() {
			@SuppressWarnings("deprecation")
			public void mouseEntered(MouseEvent e) {
				if(stat == 1) {
					Stoplb.setIcon(Stopimg);
					setCursor(Cursor.HAND_CURSOR);
				}
			}
			@SuppressWarnings("deprecation")
			public void mouseExited(MouseEvent e) {
				if(stat == 1) {
					Stoplb.setIcon(new ImageIcon("image//Stop.png"));
					setCursor(Cursor.DEFAULT_CURSOR);
				}
			}
			@SuppressWarnings("deprecation")
			public void mouseClicked(MouseEvent e) {
				if(stat == 1) {
					t.stop();
					stat = 2;
					setCursor(Cursor.DEFAULT_CURSOR);
					Beginlb.setIcon(Beginimg);
					Stoplb.setIcon(Stopimg);
					Importlb.setIcon(Importimg);
				}
			}
		});
		
		jp.add(Importlb);
		Importlb.setBounds(490, 330, Importimg.getIconWidth(), Importimg.getIconHeight());
		Importlb.addMouseListener(new MouseAdapter() {
			@SuppressWarnings("deprecation")
			public void mouseEntered(MouseEvent e) {
				if(stat != 1) {
					Importlb.setIcon(new ImageIcon("image//Importtmp.png"));
					setCursor(Cursor.HAND_CURSOR);
				}
			}
			@SuppressWarnings("deprecation")
			public void mouseExited(MouseEvent e) {
				if(stat != 1) {
					Importlb.setIcon(Importimg);
					setCursor(Cursor.DEFAULT_CURSOR);
				}
			}
			public void mouseClicked(MouseEvent e) {
				if(stat != 1) {
					NewDialog();
				}
			}
		});
		
		setVisible(true);
	}
	
	public void NewDialog() {
		JDialog jd = new JDialog(itself, "导入文件", true);
		jd.setTitle("导入文件");
		JPanel jdp = new JPanel(null);
		
		// set label
		JLabel jdb = new JLabel("请输入文件名：");
		jdp.add(jdb);
		jdb.setBounds(10, 0, 150, 40);
		jdb.setFont(new Font("华康娃娃体W5(P)", Font.PLAIN, 20));
		
		// set text
		JTextField jdtf = new JTextField("name.txt", 20);
		jdp.add(jdtf);
		jdtf.setFont(new Font("微软雅黑", Font.PLAIN, 15));
		jdtf.setBounds(10, 40, 215, 35);
		
		ImageIcon Concernimg = new ImageIcon("image//Concern.png");
		JLabel Concernlb = new JLabel(Concernimg);
		jdp.add(Concernlb);
		Concernlb.setBounds(15, 85, Concernimg.getIconWidth(), Concernimg.getIconHeight());
		Concernlb.addMouseListener(new MouseAdapter() {
			public void mouseClicked(MouseEvent e) {
				String filename = jdtf.getText();
				File file = new File(filename);
				try {
					BufferedReader br = new BufferedReader(new FileReader(file));
					String str;
					try {
						name.clear();
						while((str = br.readLine()) != null) {
							name.add(str);
						}
						jd.dispose();
					} catch (IOException e1) {
						// TODO Auto-generated catch block
						// e1.printStackTrace();
					}
				} catch (FileNotFoundException e1) {
					// TODO Auto-generated catch block
					jdb.setText("文件读取失败！");
					jdtf.setText("");
				}
			}
		});
		
		ImageIcon Cancelimg = new ImageIcon("image//Cancel.png");
		JLabel Cancellb = new JLabel(Cancelimg);
		jdp.add(Cancellb);
		Cancellb.setBounds(120, 85, Cancelimg.getIconWidth(), Cancelimg.getIconHeight());
		Cancellb.addMouseListener(new MouseAdapter() {
			public void mouseClicked(MouseEvent e) {
				jd.dispose();
			}
		});
		
		jd.setSize(250, 180);
		jd.setLocationRelativeTo(null);
		jd.setContentPane(jdp);
		jd.setVisible(true);
	}
	
	public static void main(String[] args) {
		Main m = new Main();
	}
}
