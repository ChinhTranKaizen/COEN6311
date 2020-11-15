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

@RestController
public class CarController
{
	@Autowired
	private CarService carService;
	
	
	
	@GetMapping(value="/cars")
	public Iterable<Car> getAllCars()  
	{
		return carService.getAllCars();
	}
	
	@GetMapping(value="/cars/{id}")
	public Optional<Car> getCar(@PathVariable Integer id)
	{
		return carService.getCar(id);
	}
	
	
	@PostMapping(value="/cars")
	public void addCar(@RequestBody Car car)
	{
		carService.addCar(car);
	}
	
    @PutMapping(value="/cars/{id}")
	public void updateCar(@RequestBody Car car, @PathVariable Integer id )
	{
    	carService.updateCar(id, car);
	}
	

    @DeleteMapping(value="/cars/{id}")
    public void deleteCar(@PathVariable Integer id)
	{
    	carService.deleteCar(id);
	}
	

}
