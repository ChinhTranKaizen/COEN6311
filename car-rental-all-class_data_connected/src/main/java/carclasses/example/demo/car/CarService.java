package carclasses.example.demo.car;



import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

// the service provide all the methods for the CarController class

@Service
public class CarService 
{
	@Autowired
	private CarRepository carRepository;
	
	// return all cars in DB	
	public Iterable<Car> getAllCars()
	{
		return carRepository.findAll();
	}
	//search and  return a car by id from DB
	public Optional<Car> getCar(Integer carid)
	{
		return carRepository.findById(carid);
	}
	
	// add a car to DB
	public void addCar( Car car)
	{
		carRepository.save(car);
	}
	// update a car in DB by its id 
	public void updateCar (Integer carid, Car car)
	{
		carRepository.save(car);
	}
	// delete a car from DB by its id 
	public void deleteCar( Integer carid)
	{
		carRepository.deleteById(carid);
	}

	
}
