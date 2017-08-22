/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package integracion;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Eloyo
 */
public class ConexionBD {

    
    static Connection cnn = null;
    
    
    public static Connection Enlace(Connection cn) throws SQLException{
        String ruta = "db.db";
        try{
            Class.forName("org.sqlite.JDBC");
            //File file = new File("db.Lock");
            //String prueba = file.getAbsolutePath();
            //C:\Users\Eloyo\AppData\Roaming\NetBeans\8.2\config\GF_4.1.1\domain1\config
            cn = DriverManager.getConnection("jdbc:sqlite:" + ruta);
 
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(ConexionBD.class.getName()).log(Level.SEVERE, null, ex);
        }
        return cn;
        
        
    }
}