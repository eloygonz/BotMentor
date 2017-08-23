/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package integracion;

import negocio.THorarios;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import negocio.TClase;
import negocio.THorariosC;

/**
 *
 * @author Eloyo
 */
public class DAOHorarios {
    static Connection cn;
    static Statement s;
    static  ResultSet rs;
    private THorarios transfer;
    private TClase tC;
    private String asignatura;
    
    public DAOHorarios(TClase t, String asignatura) {
        tC = t;
        this.asignatura = asignatura;
    }
    public DAOHorarios(TClase t) {
        tC = t;
    }
    /**
     * Método que devuelve todas los horarios de las asignaturas de un curso completo
     * @return 
     */
    public  ArrayList<THorariosC> getHorarios(){
        ArrayList<THorariosC> horarios = new ArrayList<THorariosC>();
        try{
           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();       
            int idA;
           String query  = "Select codigo form clases where curso = '" + tC.getCurso() + "' and GRUPO =  '" + tC.getGrupo() + "' AND GRADO = '"+ tC.getGrado() +"';";
           rs = s.executeQuery(query);
           while(rs.next()){
               THorariosC tH = new THorariosC();
               TClase t = new TClase();
               t.setId(rs.getInt("id_clase"));
               t.setIdA(rs.getInt("id_asignatura"));
               query  = "SELECT hora from horarios where id_clase = " + t.getId() + ";";
               ResultSet rs2 = s.executeQuery(query);
               while(rs2.next()){
                   tH.getHora().add(rs2.getString("hora"));
                   tH.setAula_lab(rs2.getString("aula_lab"));
               }

               query  = "SELECT nombre from asignaturas where id = " + t.getIdA() + ";";
               rs2 = s.executeQuery(query);
               tH.setAsignatura(rs2.getString("nombre"));
               horarios.add(tH);
           }    
        }catch (Exception e){
            e.printStackTrace();
        }
        return horarios; 
        
        
    }

    /**
     * Método que devuelve todos los horarios de una asignatura concreta.
     * @return 
     */
    public THorariosC getInfo() {
         THorariosC tH = new THorariosC();
        try{

           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();       
           String query  = "Select id_asignatura form clases where curso = '" + tC.getCurso() + "'" + " and GRUPO =  '" + tC.getGrupo()
                   + "' AND GRADO = '"+ tC.getGrado() +"';";
           rs = s.executeQuery(query);
           while(rs.next()){
              
               tC.setIdA(rs.getInt("id_asignatura"));
               query  = "SELECT hora from horarios where ida = " + tC.getIdA() + ";";
               ResultSet rs2 = s.executeQuery(query);
               while (rs.next()){
                   tH.getHora().add(rs2.getString("hora"));
                   tH.setAula_lab(rs2.getString("aula_lab"));
               }
               
               query  = "SELECT nombre from asignaturas where id_asignatura = " + tC.getIdA() + ";";
               rs2 = s.executeQuery(query);
               tH.setAsignatura(rs2.getString("nombre"));
           }    
        }catch (Exception e){
            e.printStackTrace();
        }
        return tH; 
    }
    /**
     * Método que devuelve todos los horarios de un curso completo, (Alternativo a GetHorarios)
     * @return 
     */
    public ArrayList<THorarios> getHorario(){
        ArrayList<THorarios> datos = new ArrayList<THorarios>();
        try{
           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();      
           /**
            * SELECT * from horarios where id_Aulas in 
            * (Select id_aulas from aulas where id_clase in 
            * (Select id_clase from clases where curso = '2ºA' and id_asignatura in 
            * (select id_asignatura from asignaturas where GRADO = 'GIS' AND siglas = 'EDA')));
            */
           String query = "SELECT * FROM horarios WHERE id_profesor in (SELECT ID_PROFESOR FROM CLASES WHERE CURSO = " +  tC.getCurso() + " and Grupo ="
                   + " '" + tC.getGrupo() + "' and GRADO = '" + tC.getGrado() +"' and id_asignatura in (SELECT id_asignatura where GRADO =' "+
                   tC.getGrado() + "' and siglas = '" + asignatura + "':";
             rs = s.executeQuery(query);
    
           while(rs.next()){
               datos.add(new THorarios(rs.getInt("ID_AULA"), rs.getString("hora"),rs.getInt("ID_CLASE"),rs.getString("AULA_LAB")));
           }
        }catch (Exception e){
            e.printStackTrace();
        }
        return datos;
        
    }
    
}
