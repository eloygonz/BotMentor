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
    private String grado;
    private String asignatura;
    private String curso;
}
