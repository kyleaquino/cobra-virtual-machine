/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cobra.ide;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import static java.lang.System.exit;
import java.net.URL;
import java.util.Optional;
import java.util.ResourceBundle;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.ButtonType;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
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
        //Image newFile = new Image(getClass().getResourceAsStream("resources/newfile.png"));
        //newButton.setGraphic(new ImageView(newFile));
    }
    
    @FXML
    private void newHover(){
        label1.setOpacity(1.00);
    }
    
    @FXML
    private void newExit(){
        label1.setOpacity(0.00);
    }
    
    @FXML
    private void openHover(){
        label2.setOpacity(1.00);
    }
    
    @FXML
    private void openExit(){
        label2.setOpacity(0.00);
    }
    
    @FXML
    private void saveHover(){
        label3.setOpacity(1.00);
    }
    
    @FXML
    private void saveExit(){
        label3.setOpacity(0.00);
    }
    
    @FXML
    private void undoHover(){
        label4.setOpacity(1.00);
    }
    
    @FXML
    private void undoExit(){
        label4.setOpacity(0.00);
    }
    
    @FXML
    private void redoHover(){
        label5.setOpacity(1.00);
    }
    
    @FXML
    private void redoExit(){
        label5.setOpacity(0.00);
    }
    
    @FXML
    private void runHover(){
        label6.setOpacity(1.00);
    }
    
    @FXML
    private void runExit(){
        label6.setOpacity(0.00);
    }
    
    @FXML
    private void buildHover(){
        label7.setOpacity(1.00);
    }
    
    @FXML
    private void buildExit(){
        label7.setOpacity(0.00);
    }
    
    @FXML
    private void bnrHover(){
        label8.setOpacity(1.00);
    }
    
    @FXML
    private void bnrExit(){
        label8.setOpacity(0.00);
    }
    
    @FXML
    private void updateWorkspace(){
        changed = true;
    }

    @FXML
    private void newFile() throws IOException{
        if (changed)
            saveFile();
	filename = null;
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
        if (file == null) {
           save("Save");
           return;
	}
        
        String text = workspace.getText();
	try (PrintWriter writer = new PrintWriter(file);){
            if (!file.canWrite())
		throw new Exception("Cannot write file!"); 
            writer.write(text);
            changed = false;
       	}catch (Exception e) {
            error.showAndWait();
	}
    }
    
    @FXML
    private void openFile() throws IOException{
        dialog = new FileChooser();
        dialog.setTitle("Open Source File");
        primaryStage = (Stage)workspace.getScene().getWindow();
        file = dialog.showOpenDialog(primaryStage);
        
        if (file != null){
            workspace.setText(read(file));
            filename.setText("FILENAME: "+file.getName());
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
        
    }
    
    
    @FXML
    private void quitProgram(){
        exit(0);
    }
    
    @FXML
    private void runProgram(){
        
    }
    
    @FXML
    private void buildProgram(){
    }
    
    @FXML
    private void runBuildProgram(){
        buildProgram();
        runProgram();
    }
    
    private String read(File file) throws IOException{
        StringBuilder stringBuffer = new StringBuilder();
        BufferedReader bufferedReader = new BufferedReader(new FileReader(file));
        String text;
        
        while ((text = bufferedReader.readLine()) != null) {
            stringBuffer.append(text);
        }

        return stringBuffer.toString();    
    }
    
    private void save(String dialogTitle) throws IOException{
        dialog.setTitle(dialogTitle);
        primaryStage = (Stage)workspace.getScene().getWindow();
        file = dialog.showSaveDialog(primaryStage);
        
        if(file!=null)
            return;
        
        FileWriter fileWriter = new FileWriter(file.getAbsoluteFile());
        fileWriter.write(workspace.getText());
        changed = false;
        primaryStage.setTitle("Cobra IDE: " + file.getName());
        filename.setText("FILENAME: "+file.getName());
         
    }
    
    
    private boolean changed = false;
    private File file;
    private FileWriter filewr;
    private PrintWriter printwr;
    private BufferedReader buffwr;
    private FileChooser dialog = new FileChooser(); 
    private Alert confirm = new Alert(AlertType.CONFIRMATION,"Do you want to save file?");
    private Alert error = new Alert(AlertType.ERROR,"Operation Error");
    private Alert success = new Alert(AlertType.INFORMATION, "Operation Success!");
    
    @FXML
    TextArea workspace = new TextArea();
    
    @FXML
    Text filename = new Text();
    
    @FXML
    Button newButton = new Button();
    
    @FXML
    Label label1, label2, label3, label4, label5, label6, label7, label8;
    
    @FXML
    AnchorPane stage;
    
    @FXML
    Stage primaryStage;
    
    
}
