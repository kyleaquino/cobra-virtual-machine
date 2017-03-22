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
import java.util.Optional;
import java.util.ResourceBundle;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextInputDialog;
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
    public void initialize(URL url, ResourceBundle rb){
        init();
    }
    
    private void init(){
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
    private void initVM() throws FileNotFoundException{
        vmDirectory();
    }
    
    @FXML
    private void runProgram() throws IOException, InterruptedException{
        if (vmdir==null){
            Alert alert = new Alert(AlertType.WARNING);
            alert.setTitle("Virtual Machine Directory");
            alert.setHeaderText("Missing VM Directory");
            alert.setContentText("Please open the Cobra++ VM main file ");
            alert.showAndWait();
            vmDirectory();
        }
            
        if(workspace.getText().equals(""))
            openFile();
        else
            saveFile();
        String args = exec(file.getAbsolutePath(), vmdir.getAbsolutePath());
        Runtime.getRuntime().exec(args);
    }
    
    @FXML
    private void printFunction(){
        if(!workspace.getText().isEmpty())
            workspace.appendText("\n");
        
        workspace.appendText(textDialog("PRINT","OUT>>","Please Input what to print"));
       
        
    }
    
    @FXML
    private void scanFunction(){
        if(!workspace.getText().isEmpty())
            workspace.appendText("\n");
        
        workspace.appendText(textDialog("SCAN","SCN>>","Please input the variable name"));
    }
    
    @FXML
    private void insertVarFunction(){
        TextInputDialog dialog = new TextInputDialog();
        dialog.setTitle("INSERT VARIABLE Function");
        dialog.setHeaderText("Please input the variable name");
        
        TextInputDialog dialog2 = new TextInputDialog();
        dialog2.setTitle("INSERT VARIABLE Function");
        dialog2.setHeaderText("Please input its value");
        

        Optional<String> result = dialog.showAndWait();
        String varName = "";
        String varValue = "";

        if (result.isPresent()) {
            varName = result.get();
        }
        
        result = dialog2.showAndWait();
        if (result.isPresent()) {
            varValue = result.get();
        }
        
        if(!workspace.getText().isEmpty())
            workspace.appendText("\n");
        
        workspace.appendText(varName+">>"+varValue);
        
    }
    
    @FXML
    private void forLoopFunction(){
        String loop = textDialog("FOR LOOP","","Input how many loops");
        String forStatement = "FOR>>"+loop+">>\n"+"//TODO"+"\n<<";
        
        
        if(!workspace.getText().isEmpty())
            workspace.appendText("\n");
        
        workspace.appendText(forStatement);
        
    }
    
    @FXML
    private void ifStatementFunction(){
        String condition = textDialog("IF STATEMENT","","Input If condition");
        String ifStatement = "IF>>"+condition+">>\n"+"//TODO"+"\n<<";
        
        if(!workspace.getText().isEmpty())
            workspace.appendText("\n");
        
        workspace.appendText(ifStatement);
    }
    
    @FXML
    private void endFunction(){
        if(!workspace.getText().isEmpty())
            workspace.appendText("\n");
        
        workspace.appendText("END");
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
    
    private void vmDirectory() throws FileNotFoundException{
        FileChooser choose = new FileChooser();
        choose.setTitle("VM Directory");
        try{
            primaryStage = (Stage)workspace.getScene().getWindow();
            vmdir = choose.showOpenDialog(primaryStage);
        }catch(Exception e){
            System.out.print(e);
        }
    }
    
    private String exec(String src, String vmdir){
        String os = System.getProperty("os.name").toLowerCase();

        String linuxExec = "xterm -hold -e python " +
                vmdir+" "+src;
        
        String winExec = "cmd /c start cmd /k python "+
                "\""+vmdir+"\""+" \""+src+"\"";
        
        if (os.contains("linux"))
            return linuxExec;
        if (os.contains("windows"))
            return winExec;
        else
            return null;
    }
    
    private String textDialog(String functionType, String statement, String headerText){
        TextInputDialog dialog = new TextInputDialog();
        dialog.setTitle(functionType+" Function");
        dialog.setHeaderText(headerText);

        Optional<String> result = dialog.showAndWait();
        String entered = "";

        if (result.isPresent()) {

            entered = result.get();
        }
        
        return (statement+entered);
    }
    
    
    private boolean changed = false;
    private File file = null; 
    private File vmdir = null;
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
