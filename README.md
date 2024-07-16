# Print Statement

![Mock-Up](docs/ps-mockup.png)

Welcome to Print Statement, a Python command line interface (CLI) application created for a small screen printing business that sells original print creations at a local market. Fully customizable, Print Statement allows users to easily update their print stock and inventory items through intuitive menus and dynamic feedback. Print statement is an efficient interface for artists and can be adapted to meet the unique needs of similar ventures. 

Run the Print Statement program [here](https://print-statement-32b6316d2a47.herokuapp.com/)

Visit associated Google Sheet [here](https://docs.google.com/spreadsheets/d/1du2cyK-pgUHrKHa2XV_88RbtFrG6MvRe8Mn8bJPPdHk/edit?gid=1680754323#gid=1680754323)

![GitHub last commit](https://img.shields.io/github/last-commit/sarahmclo/print-statement)
![GitHub language count](https://img.shields.io/github/languages/count/sarahmclo/print-statement)
![GitHub top language](https://img.shields.io/github/languages/top/sarahmclo/print-statement)

## Table of Contents
1. [User Experience (UX)](#user-experience)
    - [Project Goals](#project-goals)
    - [User stories](#user-stories)
    - [Target Audience Goals](#target-audience-goals)
    - [Site Owner Goals](#site-owner-goals)
    - [First Time User Goals](#first-time-user-goals)
    - [Return User Goals](#return-user-goals)
2. [Project Planning](#project-planning)
    - [Process](#process)
    - [Flow Chart](#flow-chart)
    - [Data Model](#data-model)
    - [Structure](#structure)
3. [Design](#design)
    - [Design Philosophy](#design-philosophy)
    - [Design Choices](#design-choices)
4. [Features](#features)
5. [Technologies Utilised](#technologies-utilised)
    - [Languages](#languages)
    - [Frameworks and Programs](#frameworks-and-programs)
6. [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Page Deployment](#page-deployment)
    - [How to Clone](#how-to-clone)
7. [Testing](#testing)
    - [Validation Testing](#validation-testing)
    - [Accessibility](#accessibility)
    - [Manual Testing](#manual-testing)
8. [Bugs and Fixes](#bugs-and-fixes)
9. [Finished Product](#finished-product)
10. [Future Features](#future-features)
11. [Credits](#credits)
    - [Content and Code](#content-and-code)
    - [Media](#media)
12. [Conclusion](#conclusion)
13. [Acknowledgements](#acknowledgements)

## User Experience (UX)<a name="user-experience"></a>

Print Statement is designed with ease of use in mind, ensuring that artists can efficiently manage their operations with minimal effort. Here are some key aspects of the user experience:

**Intuitive Interface**:
   - The command line interface (CLI) is straightforward and user-friendly, allowing users to navigate through the application with simple commands.
   - Clear prompts guide the user through each step of the process, reducing the learning curve.

**Comprehensive Management**:
   - Users can easily track daily print runs and sales, ensuring accurate records of their business activities.
   - Tables are used to organize and retrieve information about specific jobs, providing clarity and organization.

**Inventory Tracking**:
   - The application keeps detailed records of inventory levels, showing what screen print stock is available and what has been sold.
   - It highlights materials used in the printing process and indicates what needs to be restocked, helping users maintain optimal inventory levels.

**Sales and Forecasting**:
   - By analyzing sales data, Print Statement suggests what products might be needed for future markets, aiding in better planning and preparation.
   - This feature helps users make informed decisions about what to print and bring to upcoming markets.

**Customization**:
   - The application is fully customizable, allowing users to adjust print stock and inventory items as needed, it can also be adapted to suit other artist's businesses.
   - Multiple menus provide options for editing and updating various aspects of the business, ensuring the application remains relevant and useful as the business evolves.

**Efficiency**:
   - Designed to streamline the daily operations of a small screen printing business, Print Statement saves time and reduces administrative burdens.
   - Users can focus more on their creative work and customer interactions, knowing that their operational data is well-organized and easily accessible.

Overall, Print Statement enhances the user experience by providing a reliable, customizable, and efficient tool for managing the key aspects of a small screen printing business.

## Project Goals
- Develop a user-friendly CLI application to assist small screen printing businesses in managing their daily operations.
- Provide comprehensive tools for tracking print runs, sales, inventory levels, and material usage.
- Enable businesses to forecast future inventory needs based on sales data.
- Ensure the application is fully customizable to adapt to the evolving needs of each business.

## User Stories
- As a small business owner, I want to easily record and track daily print runs and sales so that I can maintain accurate business records.
- As an inventory manager, I want to monitor material usage and stock levels, so I can ensure we never run out of necessary supplies.
- As a market seller, I want to predict what products will be needed for future markets based on past sales, so I can optimize my stock and increase sales.
- As a new user, I want clear instructions and prompts, so I can quickly learn how to use the application without extensive training.
- As a frequent user, I want customizable options, so I can update my print stock and inventory items as my business changes.

## Target Audience Goals
- Efficiently manage daily operations and inventory for their screen printing business.
- Keep accurate records of sales and print runs to inform business decisions.
- Forecast future stock needs to optimize inventory and reduce waste.
- Customize the application to suit specific business needs and preferences.

## Site Owner Goals
- Provide a robust, reliable tool that meets the operational needs of small screen printing businesses.
- Ensure the application is intuitive and easy to use, reducing the time required for training and onboarding.
- Continuously improve the application based on user feedback to maintain relevance and utility.
- Support the growth and success of small screen printing businesses by streamlining their workflow.

## First Time User Goals
- Quickly understand the basic functionality and navigation of the application.
- Successfully input initial data, such as current inventory and print designs, without confusion.
- Feel confident in using the application to track daily operations after a brief learning period.
- Access clear, helpful documentation and support resources if needed.

## Return User Goals
- Easily update and modify existing data, such as adding new print designs or adjusting inventory levels.
- Quickly access and review historical sales and inventory data to inform current decisions.
- Utilize advanced features for forecasting and planning future markets based on past performance.
- Experience seamless, efficient use of the application to support ongoing business operations.

## Project Planning <a name="project-planning"></a>

| **Process**                  | **Details**|
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Conceptualization**      | - **Idea Generation**: Inspired by the need for a streamlined tool for small screen printing businesses.<br>- **Research**: Studied specific needs like inventory management, sales tracking, and forecasting. |
| **Planning**               | - **Defining Project Goals**: Outlined goals focusing on user-friendly design, comprehensive management tools, and customization.<br>- **User Stories and Target Audience Goals**: Created detailed user stories. |
| **Design**                 | - **Flow Chart Creation**: Used [Lucid Chart](https://www.lucidchart.com/pages) to visualize application structure.<br>- **Data Model Design**: Planned data model for Google Sheets integration.<br>- **Interface Design**: Designed CLI with usability and vibrant colors. |
| **Development**            | - **Setting Up Environment**: Utilized Gitpod for coding and GitHub for version control.<br>- **Implementing Core Features**: Developed print run tracking, sales management, inventory tracking, and forecasting.<br>- **Connecting to Google Sheets**: Integrated with Google Sheets using GSpread and OAuth packages. |
| **Testing**                | - **Validation Testing**: Used Pep8 Linter for code validation.<br>- **Accessibility Testing**: Used Lighthouse for accessibility testing.<br>- **Manual Testing**: Performed extensive testing across browsers and devices. |
| **Deployment**             | - **Deploying to Heroku**: Deployed the application on Heroku.<br>- **Version Control**: Used Git for version control with regular commits to GitHub.                                                      |
| **Feedback and Iteration** | - **Gathering User Feedback**: Collected initial user feedback.<br>- **Continuous Improvement**: Implemented enhancements based on feedback.                                                               |

### Flow Chart

[**Lucid Chart**](https://www.lucidchart.com/pages) was utilised to create the flowchart during project planning.

![flowchart](docs/print-statement-flowchart.png)

### Data Model - Connecting Google Sheets
### Data Model - Connecting Google Sheets

| Step Description                                                                 | Details                                                                                                                                                                       |
|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Google Drive and Sheets API Setup                                                 | Enabled via Google Cloud Platform.                                                                                                                                            |
| Credentials File Generation                                                      | Generated through the Google Drive API and added to the workspace.                                                                                                            |
| Gitignore Configuration                                                          | Added credentials file to `.gitignore` to prevent sensitive information from being pushed to the repository.                                                                  |
| Permissions Setup                                                               | Added client_email address from credentials file as an editor in Google Sheets to enable access.                                                                               |
| Variable Definition and Scope                                                    | Defined at the top of `run.py` file for accessing the worksheet.                                                                                                              |
| Package Installation                                                            | Installed GSpread and OAuth packages using terminal for interacting with Google Sheets.                                                                                       |


### Structure

| **Aspect**                  | **Details**                                                                                                                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Command Line Interface (CLI)** | - **User Interaction**: The application uses a CLI to facilitate user interaction, making it straightforward for users to input and retrieve data.<br>- **Menu Navigation**: Intuitive menus guide users through different functions, such as tracking print runs, managing inventory, and analyzing sales data. |
| **Data Storage**            | - **Google Sheets Integration**: Data is stored in Google Sheets, providing a reliable and accessible way to manage business records.<br>- **Real-time Updates**: Changes made in the application are immediately reflected in the Google Sheets, ensuring up-to-date information. |
| **Data Model**              | - **Structured Data**: Information is organized into tables within Google Sheets, making it easy to access and manipulate.<br>- **Relationship Management**: The data model ensures that relationships between different data points (e.g., inventory items and sales records) are maintained. |
| **Functionality**           | - **Print Run Tracking**: Users can log daily print runs, keeping accurate records of production.<br>- **Inventory Management**: The application tracks inventory levels, usage, and restocking needs.<br>- **Sales Analysis**: Sales data is analyzed to forecast future inventory needs and guide business decisions. |
| **Customization and Flexibility** | - **User-defined Parameters**: Users can customize various aspects of the application to fit their specific business needs, such as adding new print designs or adjusting stock levels.<br>- **Scalability**: The structure of the application allows for easy scaling as the business grows, with the ability to add more data points and complexity over time. |
| **Error Handling and Validation** | - **Input Validation**: Ensures that the data entered by users is accurate and in the correct format.<br>- **Error Messages**: Provides clear and helpful error messages to guide users in case of incorrect inputs or other issues. |

## Design <a name="design"></a>

### Design Philosophy
Print Statement is crafted with a clear and user-centric design philosophy, ensuring that it is both functional and visually engaging. Here are the core principles guiding its design:

- **User-Friendly Interface**: The command line interface (CLI) is designed to be intuitive and straightforward, making it accessible even to users with minimal technical expertise. Clear and concise prompts guide users through each function, reducing the potential for confusion and errors.

- **Visual Appeal**: The application employs bold neon colors (pink, yellow, green, and blue) to create a vibrant and engaging visual experience.
These colors are chosen not only for their aesthetic appeal but also for their ability to enhance readability and highlight important information.

- **Functionality and Efficiency**: The design prioritizes functionality, ensuring that users can quickly and easily perform tasks such as tracking print runs, managing inventory, and forecasting future needs. Streamlined menus and commands allow for efficient navigation and operation, saving users time and effort.

- **Consistency and Clarity**: Consistent use of colors and design elements helps users quickly learn and recognize different parts of the application.
Information is presented in a clear and organized manner, with important details highlighted to draw attention.

- **Customizability**: While maintaining a clear and consistent design, Print Statement allows for customization to meet the unique needs of each business. Users can easily update and modify print designs, inventory items, and other data through intuitive menus.

- **Accessibility**: The application is designed to be accessible through the Heroku command line, ensuring it can be used on various devices and platforms. The choice of bold neon colors also aims to enhance accessibility by improving visibility and contrast. By combining a user-friendly interface with vibrant, bold design elements, Print Statement ensures that managing a small screen printing business is both an efficient and enjoyable experience. The clear, concise presentation of information, coupled with the flexibility to customize, makes it a valuable tool for any small business owner. Our design philosophy centres on simplicity, vibrancy and user engagement. We believe that a clean aesthetically pleasing design enhances the user's focus on the puzzle itself.

### Design Choices
- **Minimalist Layout**: Ensures the focus remains on the necessary information.
- **Responsive Design**: Provides a seamless experience across all devices.
- **Interactive Elements**: Engages users through dynamic feedback.

## Features

### User-friendly Command Line Interface (CLI)
- **Interactive CLI**: Provides an easy-to-use interface for interacting with the application.
- **Guided Navigation**: Clear and concise menu options guide users through different functionalities of the application.

### Google Sheets Integration
- **Data Storage**: Utilizes Google Sheets for storing and managing business data.
- **Real-time Sync**: Ensures that any updates made via the application are immediately reflected in the Google Sheets.

### Comprehensive Sales Management
- **Market Sales Tracking**: Allows users to view and update daily sales data.
- **Sales Analysis**: Provides insights into sales trends to help make informed business decisions.

### Inventory Management
- **Print Stock Management**: Enables tracking of current, production, and forecasted stock levels.
- **Material Tracking**: Keeps a record of materials used in the screen printing process, ensuring that inventory levels are always up-to-date.

### Data Update Capabilities
- **Flexible Updates**: Users can update sales, stock, and material data directly from the CLI.
- **Error Handling**: Input validation and error messages ensure that the data entered is accurate and correctly formatted.

### Customization and Scalability
- **Customizable Parameters**: Users can define various parameters to tailor the application to their specific business needs.
- **Scalable Structure**: Designed to accommodate growth, allowing for the addition of new data points and increased complexity over time.

### User Feedback and Assistance
- **Typing Effect for Output**: Enhances the user experience by displaying messages in a typing animation.
- **Color-coded Messages**: Uses colorama to provide color-coded messages, making it easier for users to distinguish between different types of information and alerts.

### Clear and Informative Display
- **Tabulated Data Display**: Presents data in a clear, tabulated format using the `tabulate` module, making it easy to read and understand.

### Efficient Navigation and Program Flow
- **Main Menu Access**: Allows users to return to the main menu or exit the program at any time.
- **Loading Screens**: Informative loading messages enhance the user experience and provide feedback on the application's status.

### Robust Error Handling
- **Input Validation**: Ensures that users provide valid inputs, reducing the risk of errors and data corruption.
- **Error Messages**: Clear and helpful error messages guide users in case of incorrect inputs or issues.

### Welcome and Exit Messages
- **Welcome Screen**: A visually appealing welcome screen that introduces users to the application.
- **Exit Messages**: Informative exit messages ensure a smooth and user-friendly exit process.

### Developer Convenience
- **Clear Code Structure**: Well-organized code with comments and functions for different tasks, making it easy to maintain and extend.

## Technologies Utilised <a name="technologies-utilised"></a>

### Languages

- [**Python3**](https://en.wikipedia.org/wiki/Python_(programming_language))

Provided as part of Code Institute's [Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template)

- [**HTML5**](https://en.wikipedia.org/wiki/HTML5)
- [**Javascript**](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks and Programs

- [**Gitpod**](https://www.gitpod.io/) used for writing code, committing, and pushing to GitHub. 
- [**GitHub**](https://github.com/) utilised for hosting, viewing and some readme amendments.
- [**Lucid Chart**](https://www.lucidchart.com/pages) utilised to create the flowchart during project planning.
- [**Heroku**](https://www.heroku.com/home) used to host and deploy the finished project.
- [**PEP8**](https://ww1.pep8online.com/?usid=27&utid=6324189552) was used to validate the Python code.
- [**Colorama**](https://pypi.org/project/colorama/) was used to add colour to the terminal.
- [**GSpread**](https://docs.gspread.org/en/v6.0.0/) utilised to interact with the data in the linked sheet.
- [**Google OAuth**](https://google-auth.readthedocs.io/en/master/reference/google.oauth2.service_account.html) was used to authenticate the program in order to access Google's APIs.
- [**Google Cloud**](https://cloud.google.com/) was used to generate the APIs required to connect the data sheets with the Python code.
- [**Google Sheets**](https://docs.google.com/spreadsheets/u/0/) utilised to store user input data.
- [**Lighthouse**](https://developer.chrome.com/docs/lighthouse/overview) was used to measure the quality of the page.

## Deployment <a name="deployment"></a>

Git was used for version control. Version control was done locally and remotely. For remote version control, GitHub was used. 

### Version Control <a name="version-control"></a>
- The site was created using Gitpod editor and pushed to Github to the remote repository 'print-statement'.
- Git commands were used throughout the development to push the code to the remote repository. 
- Regular commits were made after changes:
    - git add . used to add the files to the staging area before being committed.
    - git commit -m "commit message" used to commit changes to the local repository queue.
    - git push used to push all committed code to the remote repository on Github.

### Page Deployment <a name="page-deployment"></a>
- The app was deployed with Heroku following these steps:
- After creating a Heroku account, click "New" to create a new app from the dashboard.
- Create a name of the app, that needs to be unique, and select your region. Press "Create app"
- Go to settings and add the necessary Config_vars and buildpacks. Make sure that the buildpacks are set to "Python" and "NodeJS", in that order.
- Go to Deploy tab and scroll down to Deployment Method.
- Select GitHub and search for your GitHub repository.
- Scroll down to deploy options.
- For this project the Manual Deploy method was chosen.
- Choose main branch and click Deploy Branch. This will deploy the current state of the branch specified.
- Now the app is being built and when Deploy to Heroku has a green check mark, the build is finished.
- Click View button to open the app in a browser window.

### How to Clone <a name="how-to-clone"></a>
- Go to the Github repository that you want to clone.
- Click on the Code button located above all the project files.
- Click on HTTPS and copy the repository link.
- Open the IDE of your choice and and paste the copied git url into the IDE terminal.
- The project is now created as a local clone.

## Testing <a name="testing"></a>

### Validation Testing <a name="validation-testing"></a>

Pep8 Linter Validation. No errors remain in final testing.

![markup-validation-index](docs/val-python-linter.png)

### Accessibility <a name="accessibility"></a>

Lighhouse Testing

![lighthouse-testing](docs/val-lighthouse.png)
 
### Manual Testing <a name="manual-testing"></a>

Manual testing for the site involves hands-on evaluation by human testers to ensure functionality, usability, and compatibility across various devices and browsers. By conducting the manual testing procedures below, we ensure the website functions smoothly, provides an optimal user experience, and meets desired standards.

| Testing | Description | Browser | Device | Fixed |
|-------------|-----------------------|---------|--------|----------|
| **Navigation Testing:** | bugs | Chrome, Safari, Firefox | Desktop, Laptop | Yes |
| **Performance Testing:** | bugs | Chrome, Safari, Firefox | Desktop, Laptop | Yes |

## Bugs and Fixes <a name="bugs-and-fixes"></a>

Throughout the development process, we encountered and resolved various bugs to ensure a smooth and seamless user experience. Our rigorous testing procedures helped identify and address these issues promptly.

### Python Testing Bugs ###
|Bug / Errors | Where / Location site | Browser | Device | Fixed | Solution |
|-------------|-----------------------|---------|--------|:-----:|----------|
| bugs | main.py | Chrome, Safari, Firefox | Desktop, Laptop, Tablet, Mobile | Yes  | Solution |

## Finished Product <a name="finished-product"></a>

### User-friendly CLI
- **Interactive Menu**: Easy navigation through guided menus.
- **Typing Effect**: Engaging user experience with typing animations.
- **Color-coded Feedback**: Visual distinction for better understanding.

### Google Sheets Integration
- **Real-time Data**: Instant updates and cloud storage for secure data management.

### Sales Management
- **Market Sales Tracking**: View and update daily sales data.
- **Analytics**: Insights into sales performance.

### Inventory Management
- **Print Stock**: Track current, production, and forecasted stock.
- **Materials Monitoring**: Detailed record of screens, squeegees, stencils, plastic, ink, and paper.

### Data Updates
- **Accurate Updates**: Easily update data with input validation.
- **Error Handling**: Robust mechanisms to correct invalid entries.

### User Navigation
- **Main Menu Access**: Return to the main menu or exit anytime.
- **Loading and Exit Screens**: Informative messages guide users through processes.

## Benefits

- **Efficiency**: Reduces manual effort and errors for accurate data.
- **Scalability**: Grows with your business, accommodating new data points.
- **Customization**: Adapts to specific business needs.
- **Enhanced UX**: Intuitive and enjoyable user interface.

## Future Features <a name="future-features"></a>

- **Custom Reports**: Generate custom reports for specific time frames and sales metrics.
- **Graphical Analytics**: Visualize data trends with charts and graphs.
- **User Roles**: Implement user roles and permissions for added security.
- **Collaboration Tools**: Allow multiple users to collaborate and update data simultaneously.
- **Online Sales**: Add an online sales feature.

## Credits <a name="credits"></a>

### Content and Code <a name="content-and-code"></a>

* [Code-Institute](https://codeinstitute.net/ie/?nab=0) Walkthrough projects content.
* [MDN](https://developer.mozilla.org/en-US/) Python tutorials.
* [W3 Schools](https://www.w3schools.com/python/) Python tutorials.
* [Codu](https://www.codu.co/) Inspiration.
* [Gitpod](https://www.gitpod.io/) Write, commit and push code to GitHub. 
* [GitHub](https://github.com/) Hosting, amending and viewing code.
* [Heroku](https://www.heroku.com/home) Host and deploy the finished project.
* [GSpread](https://docs.gspread.org/en/v6.0.0/) Interact with the data in the linked sheet.
* [Google OAuth](https://google-auth.readthedocs.io/en/master/reference/google.oauth2.service_account.html) Authenticate the program in order to access Google's APIs.
* [Google Cloud](https://cloud.google.com/) Generate the APIs required to connect the data sheets with the Python code.
* [Google Sheets](https://docs.google.com/spreadsheets/u/0/) Store user input data.
* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) Measure the quality of the page.
* [Real Python](https://realpython.com/) Troubleshoot python code.
* [Over API](https://overapi.com/python) Python cheatsheet.
* [PyCheckio](https://py.checkio.org/) Code practice.
* [Python Tutor](https://pythontutor.com/python-compiler.html#mode=edit) Troubleshoot code.
* [PEP8](https://ww1.pep8online.com/?usid=27&utid=6324189552) was used to validate the Python code.

### Media <a name="media"></a>
* [Convertio](https://convertio.co/) Convertio utilised to optimise images to webp for readme.
* [Colorama](https://pypi.org/project/colorama/) was used to add colour to the terminal.
* [Lucid Chart](https://www.lucidchart.com/pages) utilised to create the flowchart during project planning.

## Conclusion <a name="conclusion"></a>
Print Statement is a powerful yet user-friendly CLI application designed to support small screen printing businesses in managing their daily operations efficiently. By providing tools for tracking print runs, sales, inventory levels, and material usage, the application ensures that business owners can maintain accurate records and make informed decisions.

## Acknowledgements <a name="acknowledgements"></a>
- Amy Richardson, my course facillitator.
- Rahul Lakahanpal, my mentor.
- [Bakestock](https://github.com/amylour/BakeStock) by amylour for inspiration.
- [Budget Buddy](https://github.com/Sarah-Bue/budget-buddy) by Sarah-Bue for helpful Readme.
- Ozzy the dog, great on breaks.

[🔼 Back to top](#Print-Statement)
