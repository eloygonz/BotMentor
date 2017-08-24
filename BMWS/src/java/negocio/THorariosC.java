/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package negocio;

import java.io.Serializable;
import java.util.ArrayList;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToOne;
import javax.persistence.PrimaryKeyJoinColumn;
import javax.persistence.Table;

/**
 *
 * @author Eloyo
    CREATE TABLE Aulas_Horarios (id_aulas integer, id_clase integer REFERENCES clases(id_clase), 
*   aula_lab VARCHAR, hora VARCHAR, PRIMARY KEY (id_aulas))
 */
public class THorariosC implements Serializable{

    private int id_aula;
    private int id_clase;
    private String aula_lab;
    private String asignatura;
    private ArrayList<String> hora;

    public int getId_clase() {
        return id_clase;
    }

    public void setId_clase(int id_clase) {
        this.id_clase = id_clase;
    }

    public String getAsignatura() {
        return asignatura;
    }

    public void setAsignatura(String asignatura) {
        this.asignatura = asignatura;
    }
    
    public THorariosC(int id_aula, int id_clase, String aula_lab) {
        this.id_aula = id_aula;
        this.id_clase = id_clase;
        this.aula_lab = aula_lab;
    }

    public THorariosC() {
    }

    public int getId_asignatura() {
        return id_aula;
    }

    public void setId_asignatura(int id_asignatura) {
        this.id_aula = id_asignatura;
    }

    public ArrayList<String> getHora() {
        return hora;
    }

    public void setHora(ArrayList<String> hora) {
        this.hora = hora;
    }

    public int getId_aula() {
        return id_aula;
    }

    public void setId_aula(int id_aula) {
        this.id_aula = id_aula;
    }

    public String getAula_lab() {
        return aula_lab;
    }

    public void setAula_lab(String aula_lab) {
        this.aula_lab = aula_lab;
    }
}