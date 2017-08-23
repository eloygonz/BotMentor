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

 CREATE TABLE horarios (id_asignatura integer REFERENCES aulas_clases(id_asignatura),
 hora VARCHAR<)
 */
@Entity
@Table (name="Horarios")
public class THorarios implements Serializable{
    @Id
    @OneToOne 
    @PrimaryKeyJoinColumn(referencedColumnName = "ASIGNATURAS_codigo")
    private int id_asignatura;
    @Column(name="hora")
    private String hora;
    private int id_clase;
    private String aula_lab;

}
