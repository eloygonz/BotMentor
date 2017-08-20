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
 *
 * CREATE TABLE horarios (idA integer REFERENCES aulas_clases(idA),
 * hora VARCHAR<)
 */
@Entity
@Table (name="Horarios")
public class THorarios implements Serializable{
    @Id
    @OneToOne 
    @PrimaryKeyJoinColumn(referencedColumnName = "ASIGNATURAS_codigo")
    private int idA;
    @Column(name="hora")
    private String hora;
    private String asignatura;

    public String getAsignatura() {
        return asignatura;
    }

    public void setAsignatura(String asignatura) {
        this.asignatura = asignatura;
    }

    public int getIdA() {
        return idA;
    }

    public void setIdA(int idA) {
        this.idA = idA;
    }

    public String getHora() {
        return hora;
    }

    public void setHora(String hora) {
        this.hora = hora;
    }
    
}
