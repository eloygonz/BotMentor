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
    public static ArrayList<THorarios> getHorarios(String curso, String grupo, String grado){
        ArrayList<THorarios> horarios = new ArrayList<THorarios>();
        try{
            
           //https://web.fdi.ucm.es/Docencia/Horarios.aspx?fdicurso=2016&CodCurso=48&grupo=E&tipo=0
           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();       
           String query  = "Select codigo form clases where curso = '" + curso + "'" + " and GRUPO =  '" + grupo + "' AND GRADO = '"+ grado +"';";
           rs = s.executeQuery(query);
           while(rs.next()){
               THorarios tH = new THorarios();
               tH.setIdA(rs.getInt("codigo"));
               query  = "SELECT hora from horarios where ida = " + tH.getIdA() + ";";
               ResultSet rs2 = s.executeQuery(query);
               tH.setHora(rs2.getString("hora"));
               query  = "SELECT nombre from asignaturas where id = " + tH.getIdA() + ";";
               rs2 = s.executeQuery(query);
               tH.setAsignatura(rs2.getString("nombre"));
               horarios.add(tH);
           }    
        }catch (Exception e){
            e.printStackTrace();
        }
        return horarios; 
        
        
    }

    DAOHorarios(THorarios t){
    
    }

    public THorarios getInfo(TClase transfer) {
         THorarios tH = new THorarios();
        try{
           //https://web.fdi.ucm.es/Docencia/Horarios.aspx?fdicurso=2016&CodCurso=48&grupo=E&tipo=0
           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();       
           String query  = "Select codigo form clases where curso = '" + transfer.getCurso() + "'" + " and GRUPO =  '" + transfer.getGrupo()
                   + "' AND GRADO = '"+ transfer.getGrado() +"';";
           rs = s.executeQuery(query);
           while(rs.next()){
              
               tH.setIdA(rs.getInt("codigo"));
               query  = "SELECT hora from horarios where ida = " + tH.getIdA() + ";";
               ResultSet rs2 = s.executeQuery(query);
               tH.setHora(rs2.getString("hora"));
               query  = "SELECT nombre from asignaturas where id = " + tH.getIdA() + ";";
               rs2 = s.executeQuery(query);
               tH.setAsignatura(rs2.getString("nombre"));
           }    
        }catch (Exception e){
            e.printStackTrace();
        }
        return tH; 
    }
    
    public ArrayList<THorarios> getHorario(){
        ArrayList<THorarios> datos = new ArrayList<THorarios>();
        try{
           //https://web.fdi.ucm.es/Docencia/Horarios.aspx?fdicurso=2016&CodCurso=48&grupo=E&tipo=0
           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();      
           /**
            * SELECT * from horarios where id_Aulas in 
            * (Select id_aulas from aulas where id_clase in 
            * (Select id_clase from clases where curso = '2ºA' and id_asignatura in 
            * (select id_asignatura from asignaturas where GRADO = 'GIS' AND siglas = 'EDA')));
            */
           String Query = "SELECT * FROM horarios WHERE id_profesor in (SELECT ID_PROFESOR FROM CLASES WHERE CURSO = " +  tC.getCurso() + " and Grupo ="
                   + " '" + tC.getGrupo() + "' and GRADO = '" + tC.getGrado() +"' and id_asignatura in (SELECT id_asignatura where GRADO =' "+
                   tC.getGrado() + "' and siglas = '" + asignatura + "':";
             rs = s.executeQuery(query);
    
           while(rs.next()){
               datos.add(new THorarios(rs.getString("hora")));
           }
        }catch (Exception e){
            e.printStackTrace();
        }
        return datos;
        
    }
    
}
