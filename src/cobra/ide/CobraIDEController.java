/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cobra.ide;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import static java.lang.System.exit;
import java.net.URL;
import java.util.ResourceBundle;
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.Tooltip;
import javafx.scene.layout.AnchorPane;
import javafx.scene.text.Text;
import javafx.stage.FileChooser;
import javafx.stage.Stage;


/**
 *
 * @author kyle
 */
public class CobraIDEController implements Initializable {
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        
        initButtons();
    }
    
    private void initButtons(){
       newButton.setTooltip(new Tooltip("New"));
       saveButton.setTooltip(new Tooltip("Save"));
       openButton.setTooltip(new Tooltip("Open"));
       redoButton.setTooltip(new Tooltip("Redo"));
       undoButton.setTooltip(new Tooltip("Undo"));
       runButton.setTooltip(new Tooltip("Run"));
    }
    
    @FXML
    private void updateWorkspace(){
        changed = true;
    }

    @FXML
    private void newFile() throws IOException{
        if (changed)
            saveFile();
	filename.setText("FILENAME: ");
	workspace.setText("");
	changed = false;
    }
    
    @FXML
    private void saveFile() throws IOException{
        if (file == null)
           save("Save");
        else
            editFile();
    }
    
    @FXML
    private void openFile() throws IOException{
        FileChooser dialog = new FileChooser();
        dialog.setTitle("Open Source File");
        primaryStage = (Stage)workspace.getScene().getWindow();
        file = dialog.showOpenDialog(primaryStage);
        
        if (file != null){
            workspace.setText(read(file));
            filename.setText("FILENAME: "+file);
        }
    }
    
    @FXML
    private void undo() throws IOException{
         workspace.undo();
    }
    
    @FXML
    private void redo() throws IOException{
         workspace.redo();
    }
    
    @FXML
    private void closeFile(){
        file=null;
        filename.setText("FILENAME: ");
	workspace.setText("");
	changed = false;
    }
    
    
    @FXML
    private void quitProgram(){
        exit(0);
    }
    
    @FXML
    private void runProgram() throws IOException, InterruptedException{
        saveFile();
        String args = exec(file.getAbsolutePath());
        Runtime.getRuntime().exec(args);
    }
    
    private String read(File file) throws IOException{
        StringBuilder stringBuffer = new StringBuilder();
        BufferedReader bufferedReader = new BufferedReader(new FileReader(file));
        String text;
        
        while ((text = bufferedReader.readLine()) != null) {
            stringBuffer.append(text);
            stringBuffer.append("\n");
        }

        return stringBuffer.toString();    
    }
    
    private void save(String dialogTitle) throws IOException{
        FileChooser dialog = new FileChooser();
        dialog.setTitle(dialogTitle);
        
        primaryStage = (Stage)workspace.getScene().getWindow();
        
        file = dialog.showSaveDialog(primaryStage);
        
        try (PrintWriter fileWriter = new PrintWriter(file.getAbsoluteFile()+".cob")) {
            fileWriter.write(workspace.getText());
            changed = false;
            filename.setText("FILENAME: "+file);
        }
    }
    
    private void editFile() throws IOException{
        String text = workspace.getText();
        try (PrintWriter writer = new PrintWriter(file)) {
                writer.write(text);
                changed = false;
                filename.setText("FILENAME: "+file);
        }
    }
    
    private void saveAs() throws FileNotFoundException{
        FileChooser dialog = new FileChooser();
        dialog.setTitle("Save As");
        
        primaryStage = (Stage)workspace.getScene().getWindow();
        file = dialog.showSaveDialog(primaryStage);
        
        String text = workspace.getText();
        try (PrintWriter writer = new PrintWriter(file)) {
                writer.write(text);
                changed = false;
                filename.setText("FILENAME: "+file);
        }
    }
    
    private String exec(String src){
        String os = System.getProperty("os.name").toLowerCase();

        String linuxExec = "xterm -hold -e python " +
                System.getProperty("user.dir")+
                "/src/cobra/cobraVM/main.py "+src;
        
        String winExec = "cmd /c start cmd /k python \""+
                System.getProperty("user.dir")+
                "\\src\\cobra\\cobraVM\\main.py\" \""+src+"\"";
        
        if (os.contains("linux"))
            return linuxExec;
        if (os.contains("windows"))
            return winExec;
        else
            return null;
    }
    
    private boolean changed = false;
    private File file; 
    
    @FXML
    TextArea workspace = new TextArea();
    
    @FXML
    Text filename = new Text();
    
    @FXML
    Button newButton = new Button();
    
    @FXML
    Button openButton = new Button();
    
    @FXML
    Button saveButton = new Button();
    
    @FXML
    Button undoButton = new Button();
    
    @FXML
    Button redoButton = new Button();
    
    @FXML
    Button runButton = new Button();
    
    @FXML
    AnchorPane stage;
    
    @FXML
    Stage primaryStage;
    
    
}
