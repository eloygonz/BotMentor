/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package integracion;

import negocio.TProfesor;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

/**
 *
 * @author Eloyo
 */
public class DAOProfesor {
    
    static Connection cn;
    static Statement s;
    static  ResultSet rs;

    private TProfesor transfer;
    public DAOProfesor(TProfesor tP) {
        transfer = tP;
    }
    public DAOProfesor() {
        transfer = new TProfesor();
    }
    public TProfesor getNombre(int id) {
        try{
        cn = ConexionBD.Enlace(cn);
        s = cn.createStatement();       
        String query  = "SELECT * from profesores where id = '" + id + "';";
        rs = s.executeQuery(query);
    
        while(rs.next()){
            transfer.setNombre(rs.getString("nombre"));
            transfer.setNombre(rs.getString("id"));
            transfer.setCorreo(rs.getString("correo"));
            transfer.setDespacho(rs.getString("despacho"));
            transfer.setTlf(rs.getString("telefono"));
        }
        }catch(SQLException e){
        
    }
        return transfer;
    }
        public TProfesor getInfo() {
        try{
        cn = ConexionBD.Enlace(cn);
        s = cn.createStatement();       
        String query  = "SELECT * from profesores where nombre = '" + transfer.getNombre() + "' and apellidos = '" + transfer.getApellidos()+ "';";
        rs = s.executeQuery(query);
    
        while(rs.next()){
            transfer.setNombre(rs.getString("nombre"));
            transfer.setNombre(rs.getString("id"));
            transfer.setCorreo(rs.getString("correo"));
            transfer.setDespacho(rs.getString("despacho"));
            transfer.setTlf(rs.getString("telefono"));
        }
        }catch(SQLException e){
        
    }
        return transfer;
    }
    
}
