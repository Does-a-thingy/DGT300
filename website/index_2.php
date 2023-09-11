<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="O_index.css">
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="viewport" content="width=device-width">
        <link rel="icon" href="https://www.hhs.school.nz/wp-content/uploads/2017/09/favicon.png" sizes="32x32"/>
        <link rel="icon" href="https://www.hhs.school.nz/wp-content/uploads/2017/09/favicon.png" sizes="192x192"/>
        <title>Lost and found</title>
    </head>
    <body>
        <header class='header'>
            <a href='https://www.hhs.school.nz/' class='logo'><img src='HHS-LOGO.gif'></a>
            <h1 class='label'>Lost and Found</h1>
        </header>
        <div class='middle'>
            <div class='left'>
                <h2>Report a new find:</h2>
                <form action="" method="post" enctype="multipart/form-data">
                    <div class='name'>
                        <label>Finder's name:</label>
                        <input type="varchar" class="form-control" placeholder="Enter name" name="user_name">
                    </div>
                    <div class='place'>
                        <label>Place found:</label>
                        <input type="text" class="form-control" placeholder="Enter place" name="place">
                    </div>
                    <div class='date'>
                        <label>Date found:</label>
                        <input type="date" class="form-control" placeholder="Enter date" name="date">
                    </div>
                    <div class='object'>
                        <label>Object found:</label>
                        <input type="text" class="form-control" placeholder="Enter object" name="object">
                    </div>
                    <div class='discription'>
                        <label>Discription of find:</label>
                        <input type="text" class="form-control det" placeholder="Details (optional)" name="details">
                    </div>
                    <div class="button">
                        <input type="submit" name="insert_btn" class="btn btn-primary" ><br>
                        <a class="btn btn-primary", href='index_2.php'>View updated info</a>
                    </div>
                    <?php
                        $conn =mysqli_connect('localhost','root','','crud');
                        if(isset($_POST['insert_btn'])){
                            $user_name=$_POST['user_name'];
                            $place=$_POST['place'];
                            $date=$_POST['date'];
                            $object=$_POST['object'];
                            $details=$_POST['details'];

                            $insert ="INSERT INTO information(user_name,place,date,object_name,description)
                            VALUES('$user_name','$place','$date','$object','$details')";
                            $run_insert =mysqli_query($conn,$insert);
                        }
                    ?>
                </form>
            </div>
            <div class="right">
                <div class='find_title'>
                    <h2>Reported Finds:</h2>
                </div>
                <table class="info">
                    <tr>
                        <th>Log Id</th>
                        <th>Finders name</th>
                        <th>Place found</th>
                        <th>Date found</th>
                        <th>Object found</th>
                        <th>Details</th>
                    </tr>
                    <?php
                        $conn = mysqli_connect('localhost','root','','crud');
                        // web assisted fetching of many values
                        $sql = "SELECT * FROM information";
                        $result = $conn->query($sql);

                        if ($result->num_rows > 0) {
                          // output data of each row
                          while($row = $result->fetch_assoc()) {
                            echo "<tr> <td>" . $row["record_ID"]. "</td> <td>" . $row["user_name"]. "</td> <td>" . $row["place"]. "</td> <td>" . $row["date"].  "</td> <td>" . $row["object_name"].  "</td> <td>" . $row["description"].   "</td></tr>";
                          }
                        }
                        else {
                          echo "<tr><th></th><th>0 results</th></tr>";
                        }
                    ?>
                </table>
            </div>
        </div>
        <footer class="footer">
            <!-- directory or  navigation panel maybe -->
            <div class="listy">
                <div id="nav_menu-2" class="home">
                    <ul>
                        <li>
                            <a href="https://www.hhs.school.nz/" aria-current="page">Home</a>
                        </li>
                    </ul>
                </div>
                <!-- .footer-widget -->
                <div id="nav_menu-3" class="about">
                    <h4 class="widget-title">About</h4>
                    <ul>
                        <li>
                            <a href="https://www.hhs.school.nz/about/">About</a>
                        </li>
                        <li>
                            <a href="https://www.hhs.school.nz/from-the-principal/">From the Principal</a>
                        </li>
                        <li>
                            <a href="https://www.hhs.school.nz/staff-vacancies/">Staff Vacancies</a>
                        </li>
                        <li>
                            <a href="https://www.hhs.school.nz/from-the-chairman-of-the-board-of-trustees/">Board of Trustees</a>
                        </li>
                        <li>
                            <a href="https://www.hhs.school.nz/the-campus/">The Campus</a>
                        </li>
                        <li>
                            <a href="https://www.hhs.school.nz/henderson-high-school-foundation/">Henderson High School Foundation</a>
                        </li>
                        <li>
                            <a href="https://www.hhs.school.nz/contact-us/">Contact us</a>
                        </li>
                    </ul>
                </div>
                <!-- .footer-widget -->
                <div class="learn">
                    <h4 class="widget-title">Learn</h4>
                    <ul>
                        <li>
                            <a href="https://www.hhs.school.nz/curriculum/">Curriculum</a>
                        </li>
                        <li>
                            <a href="https://www.hhs.school.nz/sport-music-and-the-arts/">Sport, Music and the Arts</a>
                        </li>
                        <li>
                            <a href="https://www.hhs.school.nz/technology-and-21st-century-learning/">Technology and 21st Century Learning</a>
                        </li>
                        <li>
                            <a href="https://www.hhs.school.nz/academic-achievement/">Academic Achievement</a>
                        </li>
                        <li>
                            <a href="https://www.hhs.school.nz/student-leadership/">Student Leadership</a>
                        </li>
                        <li>
                            <a href="https://www.hhs.school.nz/student-support/">Student Support</a>
                        </li>
                        <li>
                            <a href="https://www.hhs.school.nz/academic-extension/">Academic Extension</a>
                        </li>
                    </ul>
                </div>
                <!-- .footer-widget -->
                <div class="apply">
                    <h4 class="widget-title">Apply</h4>
                    <ul>
                        <li>
                            <a href="https://www.hhs.school.nz/enrolling-at-henderson-high-school/">Enrolment</a>
                        </li>
                    </ul>
                </div>
                <!-- .footer-widget -->
                <div class="inter">
                    <h4 class="widget-title">International Students</h4>
                    <ul>
                        <li>
                            <a href="https://www.hhs.school.nz/welcome/">Welcome</a>
                        </li>
                        <li>
                            <a href="https://www.hhs.school.nz/what-we-offer/">What We Offer</a>
                        </li>
                        <li>
                            <a href="https://www.hhs.school.nz/testimonials/">What Students Say</a>
                        </li>
                        <li>
                            <a href="https://www.hhs.school.nz/why-choose-us/">Why Choose Us</a>
                        </li>
                        <li>
                            <a href="https://www.hhs.school.nz/homestay-programme/">Homestay Programme</a>
                        </li>
                        <li>
                            <a href="https://www.hhs.school.nz/international-student-fees/">2024 International Student Fees</a>
                        </li>
                        <li>
                            <a href="https://www.hhs.school.nz/education-in-new-zealand/">Education in New Zealand</a>
                        </li>
                    </ul>
                </div>
                <!-- .footer-widget -->
            </div>
            <div class="hhsinfo">
                <p class="loc"><b>Henderson High School</b> <br>
                    Henderson Valley <br>
                    Road PO Box 21141, Henderson <br>
                    Auckland, New Zealand</p>
                <div class="phone"><b>Phone:</b><p>+64 9 838 9085</p></div>
                <div class="fax"><b>Fax:</b><p>+64 9 838 9164</p></div>
                <div class="mail">
                    <b>Email:</b><br>
                    <a href="mailto:admin@hhs.school.nz" class='mail'>admin@hhs.school.nz</a></div>
            </div>
        </footer>
    </body>
</html>