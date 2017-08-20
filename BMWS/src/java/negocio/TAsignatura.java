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
 
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;
 
/**
 *
 * @author John
 */

@Entity
@Table(name = "ASIGNATURAS")
public class TAsignatura {
    @Id
    private int id;
    @Column(name = "NOMBRE")
    private String nombre;
    @Column(name = "SIGLAS")
    private String sigla;
    @Column(name = "GRADO")
    private String grado;

    public TAsignatura(int id, String nombre, String sigla, String grado){
        this.grado=grado;
        this.id=id;
        this.sigla=sigla;
        this.nombre=nombre;
    }
    public TAsignatura(int id){
        this.grado="";
        this.id=id;
        this.sigla="";
        this.nombre="";
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getSigla() {
        return sigla;
    }

    public void setSigla(String sigla) {
        this.sigla = sigla;
    }

    public String getGrado() {
        return grado;
    }

    public void setGrado(String grado) {
        this.grado = grado;
    }
    
}
