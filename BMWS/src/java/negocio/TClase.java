/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package negocio;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

/**
 *
 * @author Eloyo
 */
@Entity
@Table(name = "CLASES")
public class TClase {
    /*
    CREATE TABLE clases (
    "idC" INTEGER NOT NULL,
    "idP" INTEGER NOT NULL,
    "cuatri" INTEGER NOT NULL,
    "codigo" VARCHAR NOT NULL,
    "grado" VARCHAR NOT NULL,
    "curso" VARCHAR NOT NULL
    )    */
    @Id
    private int id;
    @Column(name = "idP")
    private int idP;
    @Column(name = "idA")
    private int idA;
    @Column(name = "cuatrimestre")
    private String cuatrimestre;
    @Column(name = "curso")
    private String curso;
    @Column(name = "grupo")
    private String grupo;
    
    /**
     * Entiendo que el grado pertenece a la asignatura,
     * no se si conviene o no repetir la información en las
     * tablas asignatura y clase.
     */
    @Column(name = "grado")
    private String grado;

    public TClase(int id, int idP, int idA, String cuatrimestre, String curso, String grupo, String grado) {
        this.id = id;
        this.idP = idP;
        this.idA = idA;
        this.cuatrimestre = cuatrimestre;
        this.curso = curso;
        this.grupo = grupo;
        this.grado = grado;
    }
    public TClase(int idA, String grado) {
        this.id = -1;
        this.idP = -1;
        this.idA = idA;
        this.cuatrimestre = "";
        this.curso = "";
        this.grupo = "";
        this.grado = grado;
    }
    public TClase() {
    }
    
    
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getIdP() {
        return idP;
    }

    public void setIdP(int idP) {
        this.idP = idP;
    }

    public int getIdA() {
        return idA;
    }

    public void setIdA(int idA) {
        this.idA = idA;
    }

    public String getCuatrimestre() {
        return cuatrimestre;
    }

    public void setCuatrimestre(String cuatrimestre) {
        this.cuatrimestre = cuatrimestre;
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

    public String getGrado() {
        return grado;
    }

    public void setGrado(String grado) {
        this.grado = grado;
    }


}
