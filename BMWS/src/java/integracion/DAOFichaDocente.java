/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package integracion;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import javax.jws.WebMethod;
import javax.jws.WebParam;
import negocio.TFichaDocente;

/**
 *
 * @author Eloyo
 */
public class DAOFichaDocente {

    static Connection cn;
    static Statement s;
    static  ResultSet rs;
    private TFichaDocente transfer; 
    
    public DAOFichaDocente(TFichaDocente t){
        transfer = t;
    }
    
    public String getFichaDocente() {
         String url = "no existe";
        try{
           //https://web.fdi.ucm.es/Docencia/Horarios.aspx?fdicurso=2016&CodCurso=48&grupo=E&tipo=0
           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();      
           
           String query  = "SELECT documento from fichas where asignatura in (select nombre from"
                   + " asignaturas where siglas = '" + transfer.getAsignatura() + "');";
           rs = s.executeQuery(query);
    
           while(rs.next()){
          url = rs.getString("documento");
           }
        }catch(Exception e){
                   
        }
        return url;
    }
    public ArrayList<TFichaDocente> getInfoFichas() {
        ArrayList<TFichaDocente> fichas = new ArrayList<TFichaDocente>();
        try{
           //https://web.fdi.ucm.es/Docencia/Horarios.aspx?fdicurso=2016&CodCurso=48&grupo=E&tipo=0
           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();      
           
           String query  = "SELECT * from fichas where curso = '" + transfer.getCurso() + "' AND GRADO = '" + transfer.getGrado() + "';";
           rs = s.executeQuery(query);
    
           while(rs.next()){
              TFichaDocente tF = new TFichaDocente(rs.getString("documento"), rs.getString("grado"), rs.getString("asignatura"),rs.getString("curso"));
            fichas.add(tF);
           }
        }catch(Exception e){
                   
        }
        return fichas;
    }
}
