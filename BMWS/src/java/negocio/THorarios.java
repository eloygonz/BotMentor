/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package negocio;

import java.io.Serializable;
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
@Entity
@Table (name="Horarios")
public class THorarios implements Serializable{
    @Id
    @OneToOne 
    @PrimaryKeyJoinColumn(referencedColumnName = "ASIGNATURAS_codigo")
    private int id_aula;
    @Column(name="hora")
    private String hora;
    private int id_clase;
    private String aula_lab;
    
    public THorarios(int id_aula, String hora, int id_clase, String aula_lab) {
        this.id_aula = id_aula;
        this.hora = hora;
        this.id_clase = id_clase;
        this.aula_lab = aula_lab;
    }

    public THorarios() {
    }

    public int getId_asignatura() {
        return id_aula;
    }

    public void setId_asignatura(int id_asignatura) {
        this.id_aula = id_asignatura;
    }

    public String getHora() {
        return hora;
    }

    public void setHora(String hora) {
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
