package carclasses.example.demo.car;



import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
// use the Crud Repository methods to manipulate car repository
@Repository 
public interface CarRepository extends CrudRepository<Car, Integer>{
	

}
