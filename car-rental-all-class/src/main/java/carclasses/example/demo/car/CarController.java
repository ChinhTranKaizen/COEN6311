package carclasses.example.demo.car;


import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
// use REST API to map the HTTP requests
@RestController
public class CarController
{
	@Autowired
	private CarService carService;
	
	
	// return all the cars to localhost:3001/cars
	@GetMapping(value="/cars")
	public Iterable<Car> getAllCars()  
	{
		return carService.getAllCars();
	}
	
	//return a car using its id to localhost:3001/car/id
	@GetMapping(value="/cars/{id}")
	public Optional<Car> getCar(@PathVariable Integer id)
	{
		return carService.getCar(id);
	}
	
	// receive a car from localhost:3001/cars
	@PostMapping(value="/cars")
	public void addCar(@RequestBody Car car)
	{
		carService.addCar(car);
	}
	// update a car using its id to localhost:3001/car/id
    @PutMapping(value="/cars/{id}")
	public void updateCar(@RequestBody Car car, @PathVariable Integer id )
	{
    	carService.updateCar(id, car);
	}
	
    //delete a car using its id to localhost:3001/car/id
    @DeleteMapping(value="/cars/{id}")
    public void deleteCar(@PathVariable Integer id)
	{
    	carService.deleteCar(id);
	}
	

}
