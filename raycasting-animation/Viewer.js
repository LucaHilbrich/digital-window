class Viewer
{
    constructor()
    {
        this.update();
    }

    run()
    {
        this.update();
        this.display();
    }

    update()
    {
        this.pos = createVector(mouseX - TRANSLATE_X, mouseY - TRANSLATE_Y);
        if (this.pos.x >= 0) { this.pos.x = -0.01; }
    }

    display()
    {
        fill(255);
        noStroke();
        circle(this.pos.x, this.pos.y, 10);
    }
}