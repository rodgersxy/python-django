import asyncio
import random

async def generate_random_number():
    await asyncio.sleep(1)  # Simulate an asynchronous operation
    return random.randint(1, 100)

async def main():
    # Generate three random numbers asynchronously
    random_numbers = await asyncio.gather(
        generate_random_number(),
        generate_random_number(),
        generate_random_number()
    )

    print("Generated random numbers:", random_numbers)

# Run the main function using asyncio.run()
asyncio.run(main())