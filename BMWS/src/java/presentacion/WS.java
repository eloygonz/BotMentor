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
import integracion.DAOFichaDocente;
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
import negocio.THorariosC;

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
     * consultarTutoriasC: Consulta las tutorías de una clase concreta, especificando 
     * su nombre, cuatrimeste, grado, curso y grupo.
     * @param asignatura
     * @param cuatrimestre
     * @param grado
     * @param curso
     * @param grupo
     * @return Transfer con la información de la tutoría
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
        /*
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
        */
        return tutoria;
    }
    /**
     * consultarTutoriasA :
     * Consulta todas las tutorías de una asignatura (en todos los grados)
     * @param asignatura
     * @return ArrayList con todos las tutorías existentes.
     */
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
        /*
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
        }*/
        return tutorias;
    }
    /**
     * consultarTutoriasP: Consulta todas las tutorías que da un profesor.
     * @param nombre
     * @param apellidos
     * @return Devuelve un Arraylist con la información sobre las tutorías del profesor.
     */
        @WebMethod(operationName = "consultarTutoriasP")
    public ArrayList<TTutoria> consultarTutoriasP(@WebParam(name = "nombre") String nombre, @WebParam(name = "apellidos") String apellidos) {
        ArrayList<TClase> clases = new ArrayList<TClase>();
        ArrayList<TAsignatura> asignaturas = new ArrayList<TAsignatura>();
        ArrayList<TTutoriaC> tutorias = new ArrayList<TTutoriaC>();
        TAsignatura tA;
        TTutoria tT;
        TClase tC;
        TProfesor tP = new TProfesor(nombre, apellidos);
        DAOAsignatura dA;
        DAOClase dC;
        DAOTutoria dT;
        DAOProfesor dP;
        /*A cada uno de los DAOs se les pasa un transfer con la información mínima
        necesaria para recuperar los datos solicitados. Esto se hace en cadena hasta
        recuperar todos los datos.
        */
        dP = new DAOProfesor(tP);
        tP = dP.getInfo();
        dT = new DAOTutoria();
        return dT.getInfoTutoria(tP.getId());
    }
    /**
     * consultarHorariosC: Consulta los horarios de una clase concreta, especificando grado,
     * curso y grupo.
     * @param grado
     * @param curso
     * @param grupo
     * @return ArrayList con la información de los horarios del curso
     */
        @WebMethod(operationName = "consultarHorariosC")
    public ArrayList<THorariosC> consultarHorariosC(@WebParam(name = "grado") String grado, @WebParam(name = "curso") String curso, @WebParam(name = "grupo") String grupo) {
        TClase tC = new TClase();
        tC.setCurso(curso);
        tC.setGrado(grado);
        tC.setGrupo(grupo);
        FactoriaDAO fD = FactoriaDAO.getInstance();
        DAOHorarios dH = fD.getDAOHorarios(tC,"");
        return dH.getHorarios();
    }
    /**
     * consultarHorariosA: Consulta los horarios de una asignatura concreta, especificando
     * curso, grado y grupo. 
     * @param asignatura
     * @param grado
     * @param curso
     * @param grupo
     * @return Transfer con la inforación de los horarios de dicha asignatura
     */
    @WebMethod(operationName = "consultarHorariosA")
 public THorariosC consultarHorariosA(@WebParam(name = "asignatura") String asignatura, @WebParam(name = "grado") String grado, @WebParam(name = "curso") String curso, @WebParam(name = "grupo") String grupo) {
        TClase tC = new TClase();
        tC.setCurso(curso);
        tC.setGrado(grado);
        tC.setGrupo(grupo);
        FactoriaDAO fD = FactoriaDAO.getInstance();
        DAOHorarios dH = fD.getDAOHorarios(tC,asignatura);
        return dH.getInfo();
    }
    
  /**
   * consultarClase: Método interno para obtener información sobre una clase concreta,
   * especificando curso, grado, grupo, cuatrimestre y nombre de asignatura.
   * @param curso
   * @param asignatura
   * @param grupo
   * @param cuatrimestre
   * @param grado
   * @return Transfer con la información de la asignatura.
   */
    @WebMethod(operationName = "consultarClase")
    public TClase consultarClase(@WebParam(name = "curso") String curso, @WebParam(name = "asignatura") String asignatura,
            @WebParam(name = "grupo") String grupo, @WebParam(name = "cuatrimestre") String cuatrimestre, @WebParam(name = "grado") String grado) {
        TAsignatura a = new TAsignatura(0,"",asignatura,grado);
        FactoriaDAO fD = FactoriaDAO.getInstance();
        DAOAsignatura dA = fD.getDAOAsignatura(a);
        a = dA.getCodAsignatura();
        TClase c = new TClase(a.getId(), a.getGrado());
        c.setCuatrimestre(cuatrimestre);
        c.setCurso(curso);
        c.setGrupo(grupo);
        DAOClase dC = fD.getDAOClase(c);
        return dC.getInfoClase();

    }
/**
 * consultarAsignatura: Consulta inforación sobre una asignatura (código) aportando el nombre
 * @param nombre
 * @return  Transfer con la información de la asignatura
 */
    @WebMethod(operationName = "consultarAsignatura")
    public TAsignatura consultarAsignatura(@WebParam(name = "nombre") String nombre) {
        TAsignatura a = new TAsignatura(nombre);
        FactoriaDAO fD = FactoriaDAO.getInstance();
        DAOAsignatura dao = fD.getDAOAsignatura(a);
        return dao.getInfoAsignatura();
    }
    /**
     * consultarProfesor: Consulta la información relativa a un profesor (corrreo, despacho...),
     * aportando
     * nombre y apellidos
     * @param nombre
     * @param apellidos
     * @return Transfer con la información del profesor
     */
     @WebMethod(operationName = "consultarProfesor")
    public TProfesor consultarProfesor(@WebParam(name = "nombre") String nombre, @WebParam(name = "apellidos") String apellidos) {
        TProfesor p = new TProfesor(nombre, apellidos);
        FactoriaDAO fD = FactoriaDAO.getInstance();
        DAOProfesor dao = fD.getDAOProfesor(p);
        return dao.getInfo();
    }

/**
 * consultarFichaDocenteA: Consultar la ficha docente de una asignatura (URL al documento)
 * aportando nombre de la asignatura
 * @param asignatura
 * @return String con la ruta (URL) al pdf de la ficha docente.
 */
    @WebMethod(operationName = "consultarFichaDocente")
    public String consultarFichaDocenteA(@WebParam(name = "asignatura") String asignatura) {
        TFichaDocente tF = new TFichaDocente();
        tF.setAsignatura(asignatura);
        FactoriaDAO fD = FactoriaDAO.getInstance();
        DAOFichaDocente dF = fD.getDAOFichas(tF);
        return dF.getFichaDocente();
        
    }
    /**
     * consultarFichasDocentes: Consultar las ficha docentes de un curso completo (URL a los documentos)
     * @param grado
     * @param curso
     * @return ArrayList con Transfer que contiene el nombre de las asignaturas y la ruta de la ficha
     */
        @WebMethod(operationName = "consultarFichasDocentes")
    public ArrayList<TFichaDocente> consultarFichasDocentes(@WebParam(name = "grado") String grado, @WebParam(name= "curso") String curso) {
      ArrayList<TFichaDocente> fichas = new ArrayList<TFichaDocente>();
        TFichaDocente tF = new TFichaDocente();
        tF.setCurso(curso);
        tF.setGrado(grado);
        FactoriaDAO fD = FactoriaDAO.getInstance();
        DAOFichaDocente dF = fD.getDAOFichas(tF);
        fichas = dF.getInfoFichas();
        return fichas;
    }

/**
 * consultarGrupos:Método interno para consultar los grupos existentes en un curso concreto
 * @param grado
 * @param curso
 * @return  ArrayList de Transfer con los grupos
 */
    @WebMethod(operationName = "consultarGrupos")
    public ArrayList<TCurso> consultarGrupos(@WebParam(name = "grado") String grado, @WebParam(name = "curso") String curso) {
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
 * consultarGrupo: Consulta interna para saber si un grupo existe en un curso y grado concretos
 * @param grado
 * @param curso
 * @param grupo
 * @return Transfer con la información del curso (si no existe está vacío)
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
