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
import java.util.ArrayList;

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
    public ArrayList<TTutoria> getInfoTutoria(int id_prof){
        ArrayList<TTutoria> lista = new ArrayList<TTutoria>();
        try{
           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();       
           String query;
           query = "SELECT * from tutorias where id_profesor = '"+ id_prof + "';" ;
           rs = s.executeQuery(query);
    
           while(rs.next()){
               transfer = new TTutoria();
               transfer.setIdC(rs.getInt("id_profesor"));
               transfer.setHora(rs.getString("hora"));
               transfer.setCuatrimestre(rs.getString("cuatrimestre"));
               lista.add(transfer);
           }

        }catch (Exception e){
            e.printStackTrace();
        }
        return lista;        
    }

}
