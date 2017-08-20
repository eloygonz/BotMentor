/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package negocio;

/**
 *
 * @author Eloyo
 */
public class TTutoriaC {
  
    private int idC;
    private String datos;
    private String asignatura;
    private String curso;
    private String grupo;
    private String profesor;
    private String grado;
    private String cuatrimestre;
    public TTutoriaC(int id,String dat, String asignatura, String curso, String grupo, String profesor, String grado,String cuatrimestre){
        idC = id;
        datos = dat;
        this.curso = curso;
        this.profesor = profesor;
        this.grado = grado;
        this.asignatura = asignatura;
        this.profesor = profesor;
        this.cuatrimestre = cuatrimestre;
    }

    public String getCuatrimestre() {
        return cuatrimestre;
    }

    public void setCuatrimestre(String cuatrimestre) {
        this.cuatrimestre = cuatrimestre;
    }
    public TTutoriaC(){
        
    }
    public int getIdC() {
        return idC;
    }

    public void setIdC(int idC) {
        this.idC = idC;
    }

    public String getDatos() {
        return datos;
    }

    public void setDatos(String Datos) {
        this.datos = Datos;
    }

    public String getAsignatura() {
        return asignatura;
    }

    public void setAsignatura(String asignatura) {
        this.asignatura = asignatura;
    }

    public String getCurso() {
        return curso;
    }

    public void setCurso(String curso) {
        this.curso = curso;
    }

    public String getGrupo() {
        return grupo;
    }

    public void setGrupo(String grupo) {
        this.grupo = grupo;
    }

    public String getProfesor() {
        return profesor;
    }

    public void setProfesor(String profesor) {
        this.profesor = profesor;
    }

    public String getGrado() {
        return grado;
    }

    public void setGrado(String grado) {
        this.grado = grado;
    }

}
