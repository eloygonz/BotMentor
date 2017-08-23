/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package integracion;

import negocio.TAsignatura;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

/**
 *
 * @author Eloyo
 */

public class DAOAsignatura {
private TAsignatura transfer;
    static Connection cn;
    static Statement s;
    static  ResultSet rs;

    public DAOAsignatura(TAsignatura tA) {
        
        transfer = tA;

    }
    
    public TAsignatura getInfoAsignatura(){
        

        try{

           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();       
           String query;
           query = "SELECT * FROM asignatura WHERE nombre = '" + transfer.getNombre() + "' OR sigla = '" + transfer.getSigla() + "';" ;
           rs = s.executeQuery(query);
    
           while(rs.next()){
               transfer.setId(rs.getInt("id"));
               transfer.setNombre(rs.getString("nombre"));
               transfer.setSigla(rs.getString("siglas"));
           }
        }catch (Exception e){
            e.printStackTrace();
        }
        
        return transfer;
    }
    
        public TAsignatura getAsignatura(){
        

        try{

           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();       
           String query;
           query = "SELECT * FROM asignatura WHERE id_asignatura = " + transfer.getId()+ ";" ;
           rs = s.executeQuery(query);
    
           while(rs.next()){
               transfer.setId(rs.getInt("id"));
               transfer.setGrado(rs.getString("GRADO"));
               transfer.setNombre(rs.getString("nombre"));
               transfer.setSigla(rs.getString("siglas"));
           }
        }catch (Exception e){
            e.printStackTrace();
        }
        
        return transfer;
    }
    
    public ArrayList<TAsignatura> getAsignaturas(){
        ArrayList<TAsignatura> datos = new ArrayList<TAsignatura>();
        try{ 

           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();       
           String query  = "SELECT * from asignatura where nombre =  '" + transfer.getNombre() + "' OR SIGLAS = '" +transfer.getSigla() + "';";
           rs = s.executeQuery(query);
    
           while(rs.next()){
            datos.add(new TAsignatura(rs.getInt("ID"),rs.getString("nombre"),rs.getString("siglas"),rs.getString("grado")));
           } 
            
        }catch (Exception e){
            e.printStackTrace();
        }
        
        return datos;
        
    }
    
        public TAsignatura getCodAsignatura(){
 
        try{ 

           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();       
           String query  = "SELECT * from asignatura where (nombre =  '" + transfer.getNombre() + "' OR SIGLAS = '" +transfer.getSigla() + "')"
                   + "and GRADO = '" + transfer.getGrado() + "';";
           rs = s.executeQuery(query);
    
           while(rs.next()){
            transfer = new TAsignatura(rs.getInt("ID"),rs.getString("nombre"),rs.getString("siglas"),rs.getString("grado"));
           } 
            
        }catch (Exception e){
            e.printStackTrace();
        }
        
        return transfer;
        
    }
    
}
