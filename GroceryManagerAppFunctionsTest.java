import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
	public class GroceryManagerAppFunctionsTest{
	@Test
	public void testThatAppHasNoItem(){
	GroceryManagerAppFunctions grocery = new GroceryManagerAppFunctions();
	int actual = grocery.totalNoOfItems();

	assertEquals(actual,0);
	}


	}