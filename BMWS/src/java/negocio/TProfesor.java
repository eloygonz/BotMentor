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
@Table(name="Profesor")
public class TProfesor {

    public TProfesor(String nombre, String apellidos, String despacho, String tlf, String correo) {
        this.nombre = nombre;
        this.despacho = despacho;
        this.tlf = tlf;
        this.correo = correo;
        this.apellidos = apellidos;
    }
    public TProfesor() {
        this.nombre = "";
        this.apellidos = "";
        this.despacho = "";
        this.tlf = "";
        this.correo = "";
        
    }
   
    public TProfesor(int id) {
        this.nombre = "";
        this.apellidos = "";
        this.despacho = "";
        this.tlf = "";
        this.correo = "";
        this.id = id;
    }
    public TProfesor(String nombre, String apellidos) {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.despacho = "";
        this.tlf = "";
        this.correo = "";
        this.id = id;
    }
    @Column (name="nombre")
    private String nombre;
    @Column (name="apellidos")
    private String apellidos;
    @Column (name="despacho")
    private String despacho;
    @Column (name ="tlf")
    private String tlf;
    @Column(name="correo")
    private String correo;
    @Id
    @Column(name="id")
    private int id;

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getDespacho() {
        return despacho;
    }

    public void setDespacho(String despacho) {
        this.despacho = despacho;
    }

    public String getTlf() {
        return tlf;
    }

    public void setTlf(String tlf) {
        this.tlf = tlf;
    }

    public String getCorreo() {
        return correo;
    }

    public void setCorreo(String correo) {
        this.correo = correo;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getApellidos() {
        return apellidos;
    }
    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }
}
