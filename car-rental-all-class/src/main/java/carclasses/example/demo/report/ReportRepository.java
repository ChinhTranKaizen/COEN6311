package carclasses.example.demo.report;



import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

//use the Crud Repository methods to manipulate Report repository

@Repository 
public interface ReportRepository extends CrudRepository<Report, Integer>{
	

}
