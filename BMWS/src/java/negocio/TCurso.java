package negocio;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

/**
 *
 * @author Eloy
 */
@Entity
@Table(name = "cursos")
public class TCurso {
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
    @Column(name = "grado")
    private String grado;
    @Column(name = "curso")
    private String curso;
    @Column(name = "grupo")
    private String grupo;
    
    /**
     * Entiendo que el grado pertenece a la asignatura,
     * no se si conviene o no repetir la información en las
     * tablas asignatura y clase.
     */
   

    public TCurso(int id, String curso, String grupo, String grado) {
        this.id = id;
        this.curso = curso;
        this.grupo = grupo;
        this.grado = grado;
    }
    public TCurso(String grado, String curso, String grupo) {
        this.id = -1;
        this.curso = curso;
        this.grupo = grupo;
        this.grado = grado;
    }
    public TCurso() {
    }
    
    
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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
