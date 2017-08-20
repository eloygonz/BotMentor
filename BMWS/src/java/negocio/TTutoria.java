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
    
    public TTutoria(int id,String dat){
        idC = id;
        datos = dat;
    }
    public TTutoria(){
        idC = -1;
        datos = "";
    }
    private int idC;

    public int getIdC() {
        return idC;
    }

    public void setIdC(int idC) {
        this.idC = idC;
    }

    public String getDatos() {
        return datos;
    }

    public void setDatos(String Datos) {
        this.datos = Datos;
    }
    private String datos;
    
    
}
