/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package integracion;

import negocio.TClase;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

/**
 *
 * @author Eloyo
 */
public class DAOClase {
    
    
    static Connection cn;
    static Statement s;
    static  ResultSet rs;

private TClase transfer; 
    public DAOClase(TClase tC) {
        transfer = tC;
    }
    public DAOClase() {
        transfer = new TClase();
    }
    public TClase getInfoClase(){
        try{
        cn = ConexionBD.Enlace(cn);
        s = cn.createStatement();       
        String query;
        query = "SELECT IDC,IDP FROM CLASES WHERE codigo = '" + transfer.getIdA() + "' and curso =  '"
                   + transfer.getCurso() + "' AND GRUPO = '"+ transfer.getGrupo() + "'" + " AND grado = '"+ transfer.getGrado()
                + "'" + " AND cuatrimestre = '"+ transfer.getCuatrimestre() + "'" ;
        rs = s.executeQuery(query);
    
        while(rs.next()){
            transfer.setId(rs.getInt("idC"));
            transfer.setIdP(rs.getInt("idP"));
        }
            
            
            
        }catch (Exception e){
            e.printStackTrace();
        }
        return transfer;
        
        
        
    }
    public ArrayList<TClase> getClases(){
        ArrayList<TClase> lista = new ArrayList<TClase>();
        try{
        cn = ConexionBD.Enlace(cn);
        s = cn.createStatement();       
        String query;
        query = "SELECT IDC,IDP FROM CLASES WHERE curso =  '"
                   + transfer.getCurso() + "' AND GRUPO = '"+ transfer.getGrupo() + "'" + " AND grado = '"+ transfer.getGrado()
                + "';" ;
        rs = s.executeQuery(query);
    
        while(rs.next()){
            transfer.setId(rs.getInt("idC"));
            transfer.setIdP(rs.getInt("idP"));
            lista.add(transfer);
        }
            
            
            
        }catch (Exception e){
            e.printStackTrace();
        }
        return lista;
        
        
        
    }
     public ArrayList<TClase> getClasesP(String profesor){
        ArrayList<TClase> lista = new ArrayList<TClase>();
        try{
            cn = ConexionBD.Enlace(cn);
            s = cn.createStatement();       
            String query;
            query = "SELECT * FROM CLASES WHERE IDP = '" + profesor + "';" ;
            rs = s.executeQuery(query);
    
            while(rs.next()){
                
                transfer.setId(rs.getInt("idC"));
                transfer.setIdP(rs.getInt("idP"));
            }
        }catch (Exception e){
            e.printStackTrace();
        }
        return lista;
     }
}
