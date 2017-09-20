/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package negocio;

import javax.persistence.Entity;
import javax.persistence.Table;

/**
 *
 * @author Eloyo
 */
@Entity
@Table(name="TUTORIAS")
public class TTutoria {
    
    public TTutoria(int id,String hora, String cu){
        idC = id;
        this.hora = hora;
        this.cuatrimestre = cu;
    }
    public TTutoria(){
        idC = -1;
        hora = "";
        cuatrimestre = "0";
        
    }

    public String getHora() {
        return hora;
    }

    public void setHora(String hora) {
        this.hora = hora;
    }

    public String getCuatrimestre() {
        return cuatrimestre;
    }

    public void setCuatrimestre(String cuatrimestre) {
        this.cuatrimestre = cuatrimestre;
    }
    private int idC;

    public int getIdC() {
        return idC;
    }

    public void setIdC(int idC) {
        this.idC = idC;
    }
    private String hora;
    private String cuatrimestre;
    
    
}
