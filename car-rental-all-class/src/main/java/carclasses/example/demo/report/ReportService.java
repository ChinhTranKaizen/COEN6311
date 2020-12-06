package carclasses.example.demo.report;



import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

//the service provide all the methods for the ReportController class


@Service
public class ReportService 
{
	@Autowired
	private ReportRepository reportRepository;
	
	// return all reports in DB	
		
	public Iterable<Report> getAllReports()
	{
		return reportRepository.findAll();
	}
	
	//search and  return a report by id from DB

	public Optional<Report> getReport(Integer reportid)
	{
		return reportRepository.findById(reportid);
	}
	
	// add a report to DB

	public void addReport( Report report)
	{
		reportRepository.save(report);
	}
	
	// update a report in DB by its id 

	public void updateReport( Integer reportid, Report report)
	{
		reportRepository.save(report);
	}
	
	// delete a report from DB by its id 

	public void deleteReport( Integer reportid)
	{
		reportRepository.deleteById(reportid);
	}

	
}
