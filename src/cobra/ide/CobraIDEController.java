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
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.ButtonType;
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
    private void newFile(){
        if (changed)
            saveFile();
	filename = null;
	workspace.setText("");
	changed = false;
    }
    
    @FXML
    private void saveFile(){
        Alert confirm = new Alert(AlertType.CONFIRMATION,"Do you want to save file?");
        Alert error = new Alert(AlertType.ERROR,"ERROR: Cannot Write File");
        
        if (changed) {
            Optional<ButtonType> result = confirm.showAndWait();
            if (result.get() == ButtonType.NO)
                return;
        }	
        if (file == null) {
            try {
                save(workspace.getText(),file);
            } catch (IOException ex) {
                Logger.getLogger(CobraIDEController.class.getName()).log(Level.SEVERE, null, ex);
            }
            return;
	}
        String text = workspace.getText();
	System.out.println(text);
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
        FileChooser openDialog = new FileChooser();
        openDialog.setTitle("Open Source File");
        primaryStage = (Stage)workspace.getScene().getWindow();
        file = openDialog.showOpenDialog(primaryStage);
        
        if (file != null){
            workspace.setText(read(file));
        }
     
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
    
    private void save(String text,File file) throws IOException{
        try (FileWriter fileWriter = new FileWriter(file)) {
            fileWriter.write(text);
        }
         
    }
    
    
    public boolean changed = false;
    private File file;
    
    @FXML
    TextArea workspace = new TextArea();
    
    @FXML
    Text filename = new Text();
    
    @FXML
    Button newButton = new Button();
    
    @FXML
    AnchorPane stage;
    
    @FXML
    Stage primaryStage;
    
    
}
