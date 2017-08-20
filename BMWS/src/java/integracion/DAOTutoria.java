/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package integracion;

import negocio.TTutoria;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;

/**
 *
 * @author Eloyo
 */
public class DAOTutoria {
    static Connection cn;
    static Statement s;
    static  ResultSet rs;

private TTutoria transfer;
    public DAOTutoria(TTutoria tT) {
       transfer = tT;
    }
    public DAOTutoria() {
       transfer = new TTutoria();
    }
    public TTutoria getInfoTutoria(){
        try{
           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();       
           String query;
           query = "SELECT datos from tutorias where idC = '"+ transfer.getIdC() + "';" ;
           rs = s.executeQuery(query);
    
           while(rs.next()){
               transfer.setDatos(rs.getString("datos"));
           }

        }catch (Exception e){
            e.printStackTrace();
        }
        return transfer;        
    }
    public TTutoria getTutoria(int idC){
        try{
           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();       
           String query;
           query = "SELECT datos from tutorias where idC = '"+ idC + "';" ;
           rs = s.executeQuery(query);
    
           while(rs.next()){
               transfer.setDatos(rs.getString("datos"));
           }

        }catch (Exception e){
            e.printStackTrace();
        }
        return transfer;        
    }
}
