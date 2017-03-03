/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cobra.ide;

import static java.lang.System.exit;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.text.Text;
import javafx.stage.FileChooser;

/**
 *
 * @author kyle
 */
public class CobraIDEController implements Initializable {
    
    public boolean changed = false;
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        initButtons();
        

    }
    
    private void initButtons(){
        Image newFile = new Image(getClass().getResourceAsStream("resources/newfile.png"));
        newButton.setGraphic(new ImageView(newFile));
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
        
    }
    
    @FXML
    private void openFile(){
        FileChooser dialog = new FileChooser();
        dialog.showOpenDialog(null);
     
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
    
    @FXML
    TextArea workspace = new TextArea();
    
    @FXML
    Text filename = new Text();
    
    @FXML
    Button newButton = new Button();
    
}
