/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package integracion;

import static integracion.DAOClase.cn;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import negocio.TClase;
import negocio.TCurso;

/**
 *
 * @author Eloy
 */
public class DAOCurso {
    static Connection cn;
    static Statement s;
    static  ResultSet rs;
    private TCurso transfer; 
    public DAOCurso(TCurso t) {
       transfer = t;

    }
    /**
     * CREATE TABLE Cursos (id_cursos integer not null unique, grado VARCHAR, 
        curso INTEGER NOT NULL, grupo VARCHAR, PRIMARY KEY (id_cursos))

     * @return 
     */
    public ArrayList<TCurso> getCursos(){
        ArrayList<TCurso> lista = new ArrayList<TCurso>();
        try{
            cn = ConexionBD.Enlace(cn);
            s = cn.createStatement();       
            String query;
            
            //query = "select * from cursos";
            query = "SELECT ID_CURSOS, GRUPO FROM cursos WHERE GRADO = '" + transfer.getGrado() + "' and CURSO =  "
                      + transfer.getCurso() + ";";
            rs = s.executeQuery(query);

            while(rs.next()){
                TCurso t = new TCurso();
                t.setCurso(transfer.getCurso());
                t.setGrado(transfer.getGrado());
                t.setId(rs.getInt("ID_CURSOS"));
                t.setGrupo(rs.getString("GRUPO").trim());
                lista.add(t);
            }
            
        }catch (Exception e){
            e.printStackTrace();
        }
        return lista;
    }
    public TCurso getInfoCurso(){
        try{
        cn = ConexionBD.Enlace(cn);
        s = cn.createStatement();       
        String query;
                   query = "SELECT * FROM cursos WHERE GRADO = '" + transfer.getGrado() + "' and curso =  "
                       + transfer.getCurso() + " and grupo =  '"  + transfer.getGrupo() + "';";
        rs = s.executeQuery(query);
    
        while(rs.next()){
            transfer.setId(rs.getInt("ID_CURSOS"));
            transfer.setGrupo(rs.getString("GRUPO"));
            transfer.setCurso(rs.getString("CURSO"));
            transfer.setGrado(rs.getString("GRADO"));
        }
        
        }catch (Exception e){
            e.printStackTrace();
        }
        return transfer;
        
        
        
    }
}
