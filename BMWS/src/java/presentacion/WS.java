/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package presentacion;

import negocio.TAsignatura;
import negocio.TClase;
import negocio.TFichaDocente;
import negocio.TProfesor;
import integracion.ConexionBD;
import integracion.DAOAsignatura;
import integracion.DAOClase;
import integracion.DAOCurso;
import integracion.DAOHorarios;
import integracion.DAOProfesor;
import integracion.DAOTutoria;
import integracion.FactoriaDAO;
import negocio.THorarios;
import negocio.TTutoria;
import negocio.TTutoriaC;
import java.util.ArrayList;
import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;
import java.sql.*;
import negocio.TCurso;

/**
 *
 * @author Eloyo
 */
@WebService(serviceName = "WS")
public class WS {
    static Connection cn;
    static Statement s;
    static ResultSet rs;

    /**
     * Web service operation
     */
    @WebMethod(operationName = "consultarTutoriasC")
    public TTutoriaC consultarTutoriasC(@WebParam(name = "asignatura") String asignatura,@WebParam(name = "cuatrimestre") String cuatrimestre, 
            @WebParam(name = "grado") String grado ,@WebParam(name = "curso") String curso, @WebParam(name = "grupo") String grupo) {
        
        //Creamos los Transfers involucrados en la operacion: Asignatura, tutoria y clase.
        TAsignatura tA;
        TTutoria tT;
        TClase tC;
        TTutoriaC tutoria = new TTutoriaC();
        TProfesor tP;
        //Análogamente creamos los DAOs involucrados en la operación
        DAOAsignatura daoA;
        DAOClase dC;
        DAOTutoria dT;
        DAOProfesor dP;
        /*A cada uno de los DAOs se les pasa un transfer con la información mínima
        necesaria para recuperar los datos solicitados. Esto se hace en cadena hasta
        recuperar todos los datos.
        */
        tA = new TAsignatura(0, asignatura, "", grado);
        daoA = new DAOAsignatura(tA);
        tA = daoA.getInfoAsignatura();
        tC = new TClase(tA.getId(),grado);
        dC = new DAOClase(tC);
        tC = dC.getInfoClase();
        tP = new TProfesor(tC.getIdP());
        dP = new DAOProfesor(tP);
        tutoria.setProfesor(dP.getNombre(tP.getId()).getNombre());
        tT = new TTutoria(tC.getId(),"");
        dT = new DAOTutoria(tT);
        tT = dT.getInfoTutoria();
        tutoria.setAsignatura(tA.getNombre());
        tutoria.setCurso(tC.getCurso());
        tutoria.setDatos(tT.getDatos());
        tutoria.setGrupo(tC.getGrupo());
        tutoria.setGrado(tC.getGrado());
        return tutoria;
    }
        @WebMethod(operationName = "consultarTutoriasA")
    public ArrayList consultarTutoriasA(@WebParam(name = "asignatura") String asignatura) {
        //En este caso se crean 2 listas para almacenar todas las posibles asignaturas (dependiendo
        //del grado o el cuatrimestre) y todas las posibles tutorias.
        ArrayList<TAsignatura> asignaturas = new ArrayList<TAsignatura>();
        ArrayList<TTutoriaC> tutorias = new ArrayList<TTutoriaC>();
        TAsignatura tA;
        TTutoria tT;
        TClase tC;
        TProfesor tP;
        DAOAsignatura daoA;
        DAOClase dC;
        DAOTutoria dT;
        DAOProfesor dP;
        /*A cada uno de los DAOs se les pasa un transfer con la información mínima
        necesaria para recuperar los datos solicitados. Esto se hace en cadena hasta
        recuperar todos los datos.
        */
        tA = new TAsignatura(0, asignatura, "", "");
        daoA = new DAOAsignatura(tA);
        asignaturas = daoA.getAsignaturas();
        for(int i = 0; i < asignaturas.size(); i++){
            TTutoriaC tutoria = new TTutoriaC();
            tC = new TClase(tA.getId(),asignaturas.get(i).getGrado());
            dC = new DAOClase(tC);
            tC = dC.getInfoClase();
            tP = new TProfesor(tC.getIdP());
            dP = new DAOProfesor(tP);
            tutoria.setProfesor(dP.getNombre(tP.getId()).getNombre());
            tT = new TTutoria(tC.getId(),"");
            dT = new DAOTutoria(tT);
            tT = dT.getInfoTutoria();
            tutoria.setAsignatura(tA.getNombre());
            tutoria.setCurso(tC.getCurso());
            tutoria.setDatos(tT.getDatos());
            tutoria.setGrupo(tC.getGrupo());
            tutoria.setGrado(tC.getGrado());
            tutorias.add(tutoria);
        }
        return tutorias;
    }
        @WebMethod(operationName = "consultarTutoriasP")
    public ArrayList consultarTutoriasP(@WebParam(name = "profesor") TProfesor profesor) {
        ArrayList<TClase> clases = new ArrayList<TClase>();
        ArrayList<TAsignatura> asignaturas = new ArrayList<TAsignatura>();
        ArrayList<TTutoriaC> tutorias = new ArrayList<TTutoriaC>();
        TAsignatura tA;
        TTutoria tT;
        TClase tC;
        TProfesor tP;
        DAOAsignatura dA;
        DAOClase dC;
        DAOTutoria dT;
        DAOProfesor dP;
        /*A cada uno de los DAOs se les pasa un transfer con la información mínima
        necesaria para recuperar los datos solicitados. Esto se hace en cadena hasta
        recuperar todos los datos.
        */
        dP = new DAOProfesor();
        tP = dP.getInfo(profesor.getNombre());
        dC = new DAOClase();
        clases = dC.getClasesP(tP.getNombre());
        for (int i = 0; i < clases.size(); i++){
            tC = clases.get(i);
            tA = new TAsignatura(clases.get(i).getId());
            dT = new DAOTutoria();
            tT = dT.getTutoria(clases.get(i).getId());
            tutorias.add(new TTutoriaC(tT.getIdC(),tT.getDatos(),tA.getNombre(),tC.getCurso()
            ,tC.getGrupo(),tP.getNombre(),tC.getGrado(),tC.getCuatrimestre()));
        }
        return tutorias;
    }
        @WebMethod(operationName = "consultarHorariosC")
    public ArrayList consultarHorariosC(@WebParam(name = "curso") String curso, @WebParam(name = "grupo") String grupo, @WebParam(name = "grado") String grado) {
        ArrayList<THorarios> horarios = new ArrayList<THorarios>();
        TClase tC = new TClase();
        tC.setCurso(curso);
        tC.setGrado(grado);
        tC.setGrupo(grupo);
        FactoriaDAO fD = FactoriaDAO.getInstance();
        DAOClase dC = fD.getDAOClase(tC);
        ArrayList <TClase> clases = dC.getClases();
        DAOHorarios dH = fD.getDAOHorarios();
        for (int i = 0; i < clases.size();i++){
           horarios.add(dH.getInfo(clases.get(i)));
        }
        return horarios;
    }
    
    @WebMethod(operationName = "consultarHorariosA")
 public ArrayList consultarHorariosA(@WebParam(name = "asignatura") String asignatura,@WebParam(name = "curso") String curso, @WebParam(name = "grupo") String grupo, @WebParam(name = "grado") String grado) {
     ArrayList<String> datos = new ArrayList<String>();
        try{
           //https://web.fdi.ucm.es/Docencia/Horarios.aspx?fdicurso=2016&CodCurso=48&grupo=E&tipo=0
           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();       
           String query  = "SELECT datos from horarios where idC in (Select idC form clases where curso = '" + curso + "'"
                   + " and GRUPO =  '" + grupo + "' AND GRADO = '"+ grado + "'" + " AND asignatura = '" + asignatura +"');";
           rs = s.executeQuery(query);
    
           while(rs.next()){
               datos.add(rs.getString("datos"));
           }
        }catch (Exception e){
            e.printStackTrace();
        }
        return datos;
    }
    
    /**
     * Web service operation
     */
    @WebMethod(operationName = "consultarClase")
    public TClase consultarClase(@WebParam(name = "codigo") String curso, @WebParam(name = "asignatura") String asignatura, @WebParam(name = "grupo") String grupo, @WebParam(name = "cuatrimestre") String cuatrimestre, @WebParam(name = "grado") String grado) {
        TAsignatura a = null;
        TClase c = null;
        try{
           //https://web.fdi.ucm.es/Docencia/Horarios.aspx?fdicurso=2016&CodCurso=48&grupo=E&tipo=0
           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();      
           
           String query  = "SELECT * from asignaturas where SIGLAS = '" + asignatura + "';";
           rs = s.executeQuery(query);
    
           while(rs.next()){
            String nombre = (rs.getString("NOMBRE"));
            String id = (rs.getString("ID")); // String id = (rs.getString("CODIGO"));
            String sigla = (rs.getString("SIGLAS"));
            a = new TAsignatura(Integer.parseInt(id),nombre,sigla,grado);
           }
           
           if(a!= null){
                query  = "SELECT * from clases where CURSO = '" + curso + "º" + grupo + "' AND GRADO = '"+ grado 
                        + "'" + " AND CODIGO = " + String.valueOf(a.getId()) + ";";

                rs = s.executeQuery(query);
                String datos;
                c = new TClase();
                while(rs.next()){
                    String id = (rs.getString("IDC"));
                    String idP = (rs.getString("IDP"));
                    c.setId(Integer.parseInt(id));
                    c.setIdP(Integer.parseInt(idP));
                    c.setGrupo(grupo);
                    c.setCurso(curso);
                    c.setGrado(grado);
                    c.setIdA(a.getId());
                }
           } else { 
               
               return null;
           }
            
            
        }catch (Exception e){
            e.printStackTrace();
        }
        return c;
    }
    /**
     * Web service operation
     */
    @WebMethod(operationName = "consultarAsignatura")
    public TAsignatura consultarAsignatura(@WebParam(name = "codigo") String codigo) {
        TAsignatura a = null;
        try{
           //https://web.fdi.ucm.es/Docencia/Horarios.aspx?fdicurso=2016&CodCurso=48&grupo=E&tipo=0
           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();      
           
           String query  = "SELECT * from asignaturas where codigo = '" + codigo + "';";
           rs = s.executeQuery(query);
    
           while(rs.next()){
            String nombre = (rs.getString("NOMBRE"));
            String id = (rs.getString("ID")); // String id = (rs.getString("CODIGO"));
            String sigla = (rs.getString("SIGLAS"));
            String grado = (rs.getString("GRADO"));
            a = new TAsignatura(Integer.parseInt(id),nombre,sigla,grado);
           }
        }catch(Exception e){
                   
        }
        return a;
    }
    
     @WebMethod(operationName = "consultarProfesor")
    public TProfesor consultarProfesor(@WebParam(name = "nombre") String nombre) {
        TProfesor p = null;
        try{
           //https://web.fdi.ucm.es/Docencia/Horarios.aspx?fdicurso=2016&CodCurso=48&grupo=E&tipo=0
           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();      
           
           String query  = "SELECT * from profesores where nombre = '" + nombre + "';";
           rs = s.executeQuery(query);
    
           while(rs.next()){
           p = new TProfesor(rs.getString("NOMBRE"),rs.getString("despacho"),rs.getString("telefono"),rs.getString("correo"));
           }
        }catch(Exception e){
                   
        }
        return p;
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "consultarFichaDocente")
    public String consultarFichaDocenteA(@WebParam(name = "asignatura") String asignatura) {
         String url = "no existe";
        try{
           //https://web.fdi.ucm.es/Docencia/Horarios.aspx?fdicurso=2016&CodCurso=48&grupo=E&tipo=0
           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();      
           
           String query  = "SELECT URL from fichas where asignatura = '" + asignatura + "';";
           rs = s.executeQuery(query);
    
           while(rs.next()){
          url = rs.getString("url");
           }
        }catch(Exception e){
                   
        }
        return url;
    }
        @WebMethod(operationName = "consultarFichasDocentes")
    public ArrayList consultarFichaDocente(@WebParam(name = "curso") String curso, @WebParam(name= "grado") String grado) {
         ArrayList<TFichaDocente> url = new ArrayList();
        try{
           //https://web.fdi.ucm.es/Docencia/Horarios.aspx?fdicurso=2016&CodCurso=48&grupo=E&tipo=0
           cn = ConexionBD.Enlace(cn);
           s = cn.createStatement();      
           
           String query  = "SELECT * from fichas where curso = '" + curso + "' AND GRADO = '" + grado + "';";
           rs = s.executeQuery(query);
    
           while(rs.next()){
            url.add (new TFichaDocente(rs.getString("url"), rs.getString("grado"), rs.getString("asignatura"),rs.getString("curso")));
           }
        }catch(Exception e){
                   
        }
        return url;
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "consultarGrupos")
    public ArrayList<TCurso> consultarGrupos(@WebParam(name = "curso") String curso, @WebParam(name = "grado") String grado) {
        ArrayList<TCurso> grupos = new ArrayList<TCurso>();
        TCurso tC = new TCurso();
        tC.setCurso(curso);
        tC.setGrado(grado);
        FactoriaDAO fD = FactoriaDAO.getInstance();
        DAOCurso dC = fD.getDAOCursos(tC);
        grupos = dC.getCursos();
        return grupos;
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "consultarGrupo")
    public TCurso consultarGrupo(@WebParam(name = "grado") String grado, @WebParam(name = "curso") String curso, @WebParam(name = "grupo") String grupo) {
        TCurso tC = new TCurso(grado,curso, grupo);
        FactoriaDAO fD = FactoriaDAO.getInstance();
        DAOCurso dC = fD.getDAOCursos(tC);
        tC = dC.getInfoCurso();
        return tC;
    }
}