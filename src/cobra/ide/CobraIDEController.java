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
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import static java.lang.System.exit;
import java.net.URL;
import java.util.Optional;
import java.util.ResourceBundle;
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.ButtonType;
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
       buildButton.setTooltip(new Tooltip("Build"));
       runButton.setTooltip(new Tooltip("Run"));
       buildRunButton.setTooltip(new Tooltip("Build & Run"));
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
        
        if (changed) {
            Optional<ButtonType> result = confirm.showAndWait();
            if (result.get() == ButtonType.NO)
                return;
        }
        
        if (file == null)
           save("Save");
        else
            editFile();
        
        file=null;
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
        else
            file=null;
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
        String[] args = new String[] {"/bin/bash", "-c", 
            "cd /home/kyle/NetBeansProjects/cobra-virtual-machine-master/src/cobra/cobraVM; python main.py test.vm", "with", "args"};
        
        Process proc = new ProcessBuilder(args).start();
         BufferedReader reader =  
              new BufferedReader(new InputStreamReader(proc.getInputStream()));
        String line = "", out = "";
        while((line = reader.readLine()) != null) {
            out = out + line + "\n";
            output.setText(out);
        }
        proc.waitFor(); 
    }
    
    @FXML
    private void buildProgram(){
    }
    
    @FXML
    private void runBuildProgram(){
        try {
            buildProgram();
            runProgram();
        } catch (InterruptedException | IOException ex) {
            Logger.getLogger(CobraIDEController.class.getName()).log(Level.SEVERE, null, ex);
        }
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
        
        try (FileWriter fileWriter = new FileWriter(file.getAbsoluteFile()+".cob")) {
            fileWriter.write(workspace.getText());
            changed = false;
            filename.setText("FILENAME: "+file);
        }
        
        file=null;
         
    }
    
    private void editFile() throws FileNotFoundException{

        String text = workspace.getText();
        try (PrintWriter writer = new PrintWriter(file)) {
                writer.write(text);
                changed = false;
                filename.setText("FILENAME: "+file);
        }
        
        file=null;
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
        
        file=null;
    }
    
    
    private boolean changed = false;
    private File file; 
    private final Alert confirm = new Alert(AlertType.CONFIRMATION,"Do you want to save file?");
    private final Alert error = new Alert(AlertType.ERROR,"Operation Error");
    
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
    Button buildButton = new Button();
    
    @FXML
    Button buildRunButton = new Button();
    
    @FXML
    AnchorPane stage;
    
    @FXML
    Stage primaryStage;
    
    @FXML
    TextArea output = new TextArea();
    
    
}
