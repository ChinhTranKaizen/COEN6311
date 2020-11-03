package carclasses.example.demo.car;


import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
// use the JpaRepository methods to manipulate car repository
@Repository 
public interface CarRepository extends JpaRepository<Car, Integer>{
	

}
