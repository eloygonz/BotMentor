/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package integracion;

import negocio.*;

/**
 *
 * @author Eloy
 */
public class FactoriaDAO {
   private static FactoriaDAO instance = null;
   protected FactoriaDAO() {
     
   }
   public static FactoriaDAO getInstance() {
      if(instance == null) {
         instance = new FactoriaDAO();
      }
      return instance;
   }
   public DAOAsignatura getDAOAsignatura(TAsignatura tA){
       return new DAOAsignatura(tA);
   }
   public DAOClase getDAOClase(TClase tc){
       return new DAOClase(tc);
   }
   public DAOFichaDocente getDAOFichaDocente(TFichaDocente t){
       return new DAOFichaDocente(t);
   }
   public DAOHorarios getDAOHorarios(TClase t, String asignatura){
       if(asignatura.equals("")) return new DAOHorarios(t);
       else return new DAOHorarios(t, asignatura);
   }
   public DAOProfesor getDAOProfesor(TProfesor t){
       return new DAOProfesor(t);
   }
   public DAOTutoria getDAOTutoria(TTutoria t){
       return new DAOTutoria(t);
   }
   public DAOCurso getDAOCursos(TCurso t){
       return new DAOCurso(t);
   }

   public DAOFichaDocente getDAOFichas(TFichaDocente tF) {
        return new DAOFichaDocente(tF);
   }
}
