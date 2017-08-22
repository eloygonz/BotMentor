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
public class TFichaDocente {
    private String url;

    public TFichaDocente(String url, String grado, String asignatura, String curso) {
        this.url = url;
        this.grado = grado;
        this.asignatura = asignatura;
        this.curso = curso;
    }
    public TFichaDocente(){
        
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getGrado() {
        return grado;
    }

    public void setGrado(String grado) {
        this.grado = grado;
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
            
    private String grado;
    private String asignatura;
    private String curso;
}
